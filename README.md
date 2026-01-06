# 🕵️ SentinAI: Autonomous Industrial Compliance Auditor

> **AI-Powered "Watch & Judge" System for Manufacturing & Safety Compliance.** > *Built with Google Gemini 1.5 Flash, OpenCV, and Streamlit.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![AI Engine](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange)](https://deepmind.google/technologies/gemini/)
[![Framework](https://img.shields.io/badge/Frontend-Streamlit-red)](https://streamlit.io/)

---

## 🎥 Project Demo
**(Paste your LinkedIn/YouTube Demo Video Link Here)** *Watch SentinAI in action detecting safety violations in real-time.*

![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Upload+Your+App+Screenshot+Here)
*(Tip: Replace this link with an actual screenshot of your app)*

---

## 💡 The Problem
In high-risk industries (Construction, Food Processing, Data Centers), ensuring 24/7 compliance with safety manuals is impossible for human supervisors. 
* **Manual monitoring is error-prone.**
* **CCTV feeds are passive** (they record but don't alert).
* **Safety Manuals are often ignored.**

## 🚀 The Solution: SentinAI
SentinAI is a **Multimodal RAG Agent** that bridges the gap between written rules and visual evidence.
1.  **Reads:** It digests complex PDF Safety Manuals (RAG).
2.  **Watches:** It analyzes video footage frame-by-frame using Computer Vision.
3.  **Judges:** It cross-verifies the visual action against the written rule to issue a **PASS/FAIL** verdict.

---

## 🧪 Tested Use Cases

| Scenario | Rule Source (PDF) | Visual Detection Target |
| :--- | :--- | :--- |
| **Data Security** | Section 4: "No Mobile Phones in Server Room" | Detects smartphone usage. |
| **Food Hygiene** | Section 1: "Mandatory Hand Wash" | Verifies hand-rubbing motion vs direct food contact. |
| **PPE Compliance** | Section 2: "Mandatory Hard Hat / Helmet" | Detects missing safety gear on workers. |

---

## 🛠️ Tech Stack
* **LLM & Vision:** Google Gemini 1.5 Flash (Multimodal)
* **Vector Search (RAG):** PyPDF & In-context Learning
* **Video Processing:** OpenCV (Frame extraction & encoding)
* **Interface:** Streamlit (Python)

---

## 💻 Installation & Setup
Since this project uses a paid/metered API, it is designed to run locally.

**1. Clone the Repository**
```bash
git clone [https://github.com/scarwill/SentinAI-Auditor.git](https://github.com/scarwill/SentinAI-Auditor.git)
cd SentinAI-Auditor