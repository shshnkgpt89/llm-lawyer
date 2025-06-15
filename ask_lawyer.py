import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

load_dotenv()

def answer_question(question):
    embeddings = HuggingFaceEmbeddings()
    db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    docs = db.similarity_search(question, k=4)

    if not docs:
        return "❌ No relevant documents found."

    llm = ChatOpenAI(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model_name="llama3-8b-8192",  # ✅ Fast Groq model that works reliably
        temperature=0.1,
        max_tokens=1024,
    )

    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=question)
    return response
