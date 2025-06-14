import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def process_and_index_documents(file_paths):
    all_docs = []

    for file_path in file_paths:
        # Load PDF content
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        all_docs.extend(docs)

    # Initialize embedding model
    embeddings = HuggingFaceEmbeddings()

    # Create or update Chroma DB
    db = Chroma.from_documents(
        documents=all_docs,
        embedding=embeddings,
        persist_directory="chroma_db"
    )
    db.persist()
