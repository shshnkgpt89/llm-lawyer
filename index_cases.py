from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

# Load the "dutch co agreement.pdf"
pdf_path = "uploads/dutch co agreement.pdf"
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"❌ File not found: {pdf_path}")

# Load documents from PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Save into Chroma vector DB
vectorstore = Chroma.from_documents(documents, embeddings, persist_directory="chroma_db")
vectorstore.persist()

print("✅ 'Dutch Co Agreement' has been indexed successfully.")
