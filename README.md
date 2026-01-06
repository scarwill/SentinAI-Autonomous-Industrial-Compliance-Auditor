# 🕵️ SentinAI: Autonomous Industrial Compliance Auditor

> **AI-Powered "Watch & Judge" System for Manufacturing Safety.**
> *Built with Google Gemini 1.5 Flash (Multimodal), OpenCV, and Streamlit.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![AI Engine](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Framework](https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## 📸 Dashboard Preview
A real-time view of SentinAI detecting a safety violation by cross-referencing the PDF manual.

![Project Dashboard](./dashboard.png)

---

## 🎥 Live Project Demo
### 👉 [Click Here to Watch the Full Video Walkthrough](./Demo.mp4) 👈
*(This video demonstrates the AI processing the manual, analyzing footage, and generating a Pass/Fail verdict in real-time.)*

---

## 💡 The Problem
In high-risk industries (Construction, Food Processing, Data Centers), ensuring 24/7 compliance with safety manuals is impossible for human supervisors.
* **Manual monitoring is error-prone.**
* **CCTV feeds are passive** (they record but don't alert).
* **Safety Manuals are often ignored** (PDFs are not actionable).

## 🚀 The Solution: SentinAI
SentinAI is a **Multimodal RAG Agent** that bridges the gap between written rules and visual evidence.

1.  **Reads (RAG):** It digests complex PDF Safety Manuals to understand the rules.
2.  **Watches (Vision):** It analyzes video footage frame-by-frame using Computer Vision.
3.  **Judges (Reasoning):** It cross-verifies the visual action against the written rule to issue a **PASS/FAIL** verdict with an explanation.

---

## 📂 Repository Contents
This repository contains the source code and **sample test videos** so you can run the audit immediately.

* `app.py` - Main Application Logic
* `safety_manual.pdf` - The "Employee Handbook" (Source of Truth)
* `requirements.txt` - Project Dependencies
* `dashboard.png` - App Screenshot
* `demo_video.mp4` - Full Project Demo

---

## 🧪 Test Scenarios (Included Videos)

You can use the videos provided in this repo to test specific compliance rules:

| Test Scenario | Video Preview (Click to Play) | Input Query to Type | Expected Result |
| :--- | :--- | :--- | :--- |
| **1. Data Security** | [▶️ Watch Mobile Violation](./mobile_violation.mp4) | `mobile phone` | **FAIL** ❌ (Phone detected) |
| **2. Food Hygiene** | [▶️ Watch Hygiene Violation](./hygiene_violation.mp4) | `hand wash` | **FAIL** ❌ (No hand wash) |
| **3. PPE Safety** | [▶️ Watch Helmet Violation](./ppe_violation.mp4) | `helmet` / `hard hat` | **FAIL** ❌ (No Headgear) |

---

## 💻 Installation & Setup

**1. Clone the Repository**
```bash
git clone [https://github.com/scarwill/SentinAI-Auditor.git](https://github.com/scarwill/SentinAI-Auditor.git)
cd SentinAI-Auditor
