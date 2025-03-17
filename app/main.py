import streamlit as st
from auth import authentication_flow
from chat_utils import display_messages, handle_user_input, init_chat_history
from db.base import init_db
from vertexai_utils import init_model, init_vertexai


def main() -> None:
    init_db()

    init_vertexai()
    model = init_model()

    if not authentication_flow():
        st.stop()

    st.set_page_config(page_title="Chatbot", page_icon="🤖")
    st.title("Chatbot 🤖")
    st.write("Welcome to the chatbot! Ask me anything.")

    init_chat_history()
    display_messages()
    handle_user_input(model)


if __name__ == "__main__":
    main()
