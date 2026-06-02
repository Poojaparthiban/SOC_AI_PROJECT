import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI-Powered Cyber Threat Detection and SOC Analyst Assistant")

log = st.text_area("Paste Security Log")

if st.button("Analyze Threat"):

    prompt = f"""
    You are a SOC Analyst.

    Analyze the following security log and provide:

    1. Threat Type
    2. Severity (Low/Medium/High)
    3. MITRE ATT&CK Mapping
    4. Recommendations

    Security Log:
    {log}
    """

    response = model.generate_content(prompt)

    st.subheader("AI Analysis Result")
    st.write(response.text)