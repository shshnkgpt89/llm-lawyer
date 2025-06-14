import streamlit as st
from ask_lawyer import answer_question

st.set_page_config(page_title="Legal Chat", layout="wide")
st.title("📚 Legal Assistant - Chat")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box
user_input = st.chat_input("Ask a legal question...")

# Process input
if user_input:
    # Append user's question
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get LLM response
    response = answer_question(user_input)
    
    # Append LLM's answer
    st.session_state.messages.append({"role": "ai", "content": response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"🧑‍💼 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **Legal AI:** {message['content']}")



