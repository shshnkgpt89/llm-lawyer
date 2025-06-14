import streamlit as st
import os
from index_cases import process_and_index_documents

st.set_page_config(page_title="📚 Sources", layout="wide")
st.title("📚 Upload Legal Case PDFs")

# Create uploads folder if not exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Upload PDFs
uploaded_files = st.file_uploader(
    "Upload PDF files", type="pdf", accept_multiple_files=True
)

# Handle and index PDFs
if uploaded_files:
    saved_files = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join("uploads", uploaded_file.name)

        # Save file to disk
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_files.append(file_path)

        # Store file name in session state
        if "uploaded_file_names" not in st.session_state:
            st.session_state.uploaded_file_names = []

        if uploaded_file.name not in st.session_state.uploaded_file_names:
            st.session_state.uploaded_file_names.append(uploaded_file.name)

    # Index files
    process_and_index_documents(saved_files)
    st.success("✅ Files uploaded and indexed successfully!")

# Show uploaded files
st.subheader("📁 Uploaded and Indexed Files")
if "uploaded_file_names" in st.session_state and st.session_state.uploaded_file_names:
    for file_name in st.session_state.uploaded_file_names:
        st.markdown(f"- 📄 {file_name}")
else:
    st.info("No files uploaded yet.")


