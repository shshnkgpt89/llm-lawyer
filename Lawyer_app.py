import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Title and Introduction
st.title("⚖️ Welcome to Legal Assistant")
st.markdown("""
This assistant allows you to:

1. 📤 Upload legal PDF case documents  
2. 💬 Ask legal questions and get responses using local LLM  
3. 🛡️ All data stays 100% offline (local hosting)

👉 Use the sidebar to switch between **Sources** and **Chat**
""")
