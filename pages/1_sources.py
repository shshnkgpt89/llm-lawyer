import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Constants
UPLOAD_FOLDER = "uploads"
BASE_FOLDER = "base_documents"
CHROMA_DB_DIR = "chroma_db"

# Page Config
st.set_page_config(page_title="Upload Legal Sources", layout="wide")
st.title("📄 Upload Legal Documents")

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BASE_FOLDER, exist_ok=True)

# File uploader
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

# Save uploaded PDFs
if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(UPLOAD_FOLDER, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
    st.success("✅ Files uploaded successfully.")
    st.info("🔄 Indexing documents. Please wait...")

# Load & index PDFs
documents = []

# Load base documents
for filename in os.listdir(BASE_FOLDER):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(BASE_FOLDER, filename))
        docs = loader.load()
        documents.extend(docs)

# Load uploaded documents
for filename in os.listdir(UPLOAD_FOLDER):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(UPLOAD_FOLDER, filename))
        docs = loader.load()
        documents.extend(docs)

# ✅ Print how many docs were indexed
print(f"📄 Indexed docs count: {len(documents)}")

# ✅ Bonus: Show which files were indexed
print("📂 Files processed:")
for filename in os.listdir(BASE_FOLDER):
    if filename.endswith(".pdf"):
        print("  • base_documents/" + filename)
for filename in os.listdir(UPLOAD_FOLDER):
    if filename.endswith(".pdf"):
        print("  • uploads/" + filename)

# Generate embeddings and persist to Chroma
if documents:
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(documents, embeddings, persist_directory=CHROMA_DB_DIR)
    db.persist()
    st.success("✅ Documents indexed and stored in vector database.")
else:
    st.warning("⚠️ No documents found to index.")
