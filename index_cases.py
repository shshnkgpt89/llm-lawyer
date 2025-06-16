import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

UPLOAD_FOLDER = "uploads"
BASE_FOLDER = "base_documents"
ALL_DOCS = []

def load_documents_from(folder):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder, filename))
            docs.extend(loader.load())
    return docs

ALL_DOCS.extend(load_documents_from(BASE_FOLDER))
ALL_DOCS.extend(load_documents_from(UPLOAD_FOLDER))

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(ALL_DOCS, embeddings, persist_directory="chroma_db")
db.persist()
print("✅ All documents indexed including base documents.")

