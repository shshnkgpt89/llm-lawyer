import streamlit as st
from ask_lawyer import answer_question

st.set_page_config(page_title="Legal Assistant - Chat", layout="wide")
st.title("💬 Chat with Legal Assistant")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input from user
user_input = st.text_input("Ask a question about the 'Dutch Co Agreement':", key="input")

# When the user submits a question
if user_input:
    with st.spinner("Thinking..."):
        response = answer_question(user_input)
    
    # Save both user input and AI response in chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑‍💼 {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")
