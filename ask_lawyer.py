from langchain_community.llms import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def answer_question(question):
    # Load embeddings
    embeddings = HuggingFaceEmbeddings()

    # Load vector store
    db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

    # Retrieve top 4 most relevant document chunks
    docs = db.similarity_search(question, k=4)

    if not docs:
        return "❌ I couldn’t find anything relevant to your question in the uploaded documents."

    # Load Gemma model
    llm = Ollama(model="phi3")

    # Format prompt for Gemma
    chain = load_qa_chain(llm, chain_type="stuff")

    # Run QA chain
    response = chain.run(input_documents=docs, question=question)

    return response
