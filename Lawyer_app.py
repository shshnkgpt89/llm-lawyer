import streamlit as st

st.set_page_config(
    page_title="Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Welcome to Legal Assistant")

st.markdown("""
This assistant allows you to:

1. 📤 Upload legal PDF case documents  
2. 💬 Ask legal questions and get answers from your documents  
3. 🛡️ 100% local processing with Groq-hosted LLaMA3

👉 Use the sidebar to switch between **Sources** and **Chat**
""")

