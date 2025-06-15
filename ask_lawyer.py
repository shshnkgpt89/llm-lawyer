from langchain_community.llms import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize components once (best for performance)
embeddings = HuggingFaceEmbeddings()
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

llm = Ollama(
    model="phi3",
    temperature=0.2,
    num_predict=256,
    stop=["\nUser:"],
    streaming=False
)

chain = load_qa_chain(llm, chain_type="stuff")

def answer_question(question: str) -> str:
    # Search for top 4 relevant chunks
    docs = db.similarity_search(question, k=4)

    if not docs:
        return "❌ Sorry, I couldn't find anything relevant in the Dutch Co Agreement."

    # Run the QA chain
    response = chain.run(input_documents=docs, question=question)
    return response.strip()
