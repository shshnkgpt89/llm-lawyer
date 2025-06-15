from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def process_and_index_documents(uploaded_files=None):
    documents = []

    if uploaded_files:
        # Handle uploaded PDFs from UI
        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        for uploaded_file in uploaded_files:
            file_path = os.path.join("uploads", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    else:
        # Fallback to "dutch co agreement.pdf"
        pdf_path = "uploads/dutch co agreement.pdf"
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"❌ File not found: {pdf_path}")

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

    # Split the documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Create and persist vector DB
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory="chroma_db")
    vectorstore.persist()

    return True
