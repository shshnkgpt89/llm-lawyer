import streamlit as st
from ask_lawyer import answer_question

st.set_page_config(page_title="Legal Assistant - Chat", layout="wide")
st.title("🤖 Chat with Legal Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "ai", "message": "Hi! Ask me anything about your legal documents 📄"}]

user_input = st.chat_input("Ask a legal question...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "message": user_input})

    with st.spinner("Thinking..."):
        try:
            ai_response = answer_question(user_input)
        except Exception as e:
            ai_response = f"⚠️ Error: {str(e)}"

    st.session_state.chat_history.append({"role": "ai", "message": ai_response})

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["message"])
