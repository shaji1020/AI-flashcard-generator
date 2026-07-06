from dotenv import load_dotenv
import os

load_dotenv()
import streamlit as st
import google.generativeai as genai

API_KEY = os.getenv("GCP_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📚 AI Flashcard Generator")
st.write("Paste your notes and generate study flashcards instantly.")

notes = st.text_area("Paste your notes here")

if st.button("Generate Flashcards"):
    prompt = f"""
Convert the following notes into study flashcards.

Rules:
- Create 5 flashcards
- Format as:

Q: question
A: answer

Notes:
{notes}
"""

response = model.generate_content(prompt)
st.write(response.text)