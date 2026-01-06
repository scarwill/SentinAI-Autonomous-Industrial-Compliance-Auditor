import streamlit as st
import cv2
import os
import tempfile
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
from pypdf import PdfReader

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="SentinAI Auditor", page_icon="🕵️", layout="wide")

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# --- MODEL SELECTION ---
# Using 'gemini-flash-latest' for stability and higher rate limits in production.
MODEL_NAME = 'gemini-flash-latest'

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    if api_key:
        st.success("API Key Loaded ✅")
        genai.configure(api_key=api_key)
        
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            st.info(f"✅ Active Model: {MODEL_NAME}")
        except Exception as e:
            st.error(f"Model Error: {e}")
            
    else:
        st.error("API Key Missing! Please check your .env file.")
        st.stop()
    
    st.info("💡 **Tip:** This AI compares 'Video Evidence' against 'PDF Manual Rules'.")

# --- 2. BACKEND LOGIC ---

def get_pdf_text(pdf_file):
    """Extracts text from the uploaded PDF manual."""
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_rule(text, topic):
    """Uses LLM to find the specific rule related to the topic in the manual."""
    prompt = f"""
    Manual Content: \"\"\"{text}\"\"\"
    Extract the specific rule regarding '{topic}'. Summarize in 1 sentence.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error extracting rule: {e}"

def analyze_compliance(image_path, rule):
    """Uses Vision LLM to compare the image against the extracted rule."""
    with PIL.Image.open(image_path) as img:
        prompt = f"""
        Rule: "{rule}"
        Analyze the image. 
        If the person follows the rule, output STATUS: PASS.
        If they break the rule, output STATUS: FAIL.
        Also provide a short OBSERVATION and VERDICT.
        """
        try:
            response = model.generate_content([prompt, img])
            return response.text
        except Exception as e:
            return f"Error analyzing image: {e}"

# --- 3. FRONTEND UI ---

st.title("🕵️ SentinAI: Industrial Compliance Auditor")
st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📂 Step 1: Upload Data")
    uploaded_pdf = st.file_uploader("Upload Safety Manual (PDF)", type=["pdf"])
    uploaded_video = st.file_uploader("Upload CCTV Footage (MP4)", type=["mp4"])
    target_topic = st.text_input("Rule to Check", "mobile phone")

with col2:
    st.subheader("👀 Preview")
    if uploaded_video:
        st.video(uploaded_video)

# --- 4. EXECUTION ---

if st.button("🚀 Run Compliance Audit", type="primary"):
    if not uploaded_pdf or not uploaded_video:
        st.warning("Please upload both Video and PDF first!")
    else:
        with st.spinner("🤖 AI Auditor is working... Please wait..."):
            
            # A. Process PDF
            pdf_text = get_pdf_text(uploaded_pdf)
            rule = extract_rule(pdf_text, target_topic)
            st.success(f"**Extracted Rule:** {rule}")
            
            # B. Process Video (Temp File Handling for OpenCV)
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') 
            tfile.write(uploaded_video.read())
            tfile.close() 
            
            cap = cv2.VideoCapture(tfile.name)
            
            if not cap.isOpened():
                st.error("Error: Could not load video file.")
            else:
                # Extract the middle frame for analysis
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames // 2)
                
                ret, frame = cap.read()
                cap.release()
                
                if ret:
                    frame_path = "audit_frame.jpg"
                    cv2.imwrite(frame_path, frame)
                    
                    # C. Final AI Judgement
                    result = analyze_compliance(frame_path, rule)
                    
                    st.divider()
                    st.subheader("📊 Audit Results")
                    
                    res_col1, res_col2 = st.columns([1, 1])
                    with res_col1:
                        st.image(frame_path, caption="Analyzed Frame", width="stretch")
                    with res_col2:
                        st.markdown(f"**Applied Rule:**\n> *{rule}*")
                        if "PASS" in result:
                            st.success(result)
                        else:
                            st.error(result)
                    
                    # Cleanup Frame Image
                    if os.path.exists(frame_path):
                        os.remove(frame_path)
            
            # Cleanup Temp Video File
            if os.path.exists(tfile.name):
                try:
                    os.remove(tfile.name)
                except:
                    pass