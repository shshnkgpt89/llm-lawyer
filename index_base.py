import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_DB_DIR = "chroma_db"
BASE_DOCS_DIR = "base_documents"

print("🔁 Re-indexing base documents...")

documents = []
for filename in os.listdir(BASE_DOCS_DIR):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(BASE_DOCS_DIR, filename))
        docs = loader.load()
        documents.extend(docs)

print(f"✅ Loaded {len(documents)} chunks from base documents.")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(documents, embeddings, persist_directory=CHROMA_DB_DIR)
db.persist()

print("✅ Chroma DB re-indexed and saved.")
