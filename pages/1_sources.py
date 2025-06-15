import streamlit as st
from index_cases import process_and_index_documents

st.set_page_config(page_title="Sources", page_icon="📚")

st.title("📚 Upload Sources")

st.write("You can upload additional legal documents to use in chat.")

uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if st.button("Index Documents"):
    with st.spinner("Processing and indexing documents..."):
        process_and_index_documents(uploaded_files)
    st.success("Files uploaded and indexed successfully!")
else:
    st.info("Even if you don't upload anything, 'Dutch Co Agreement' will be available.")
