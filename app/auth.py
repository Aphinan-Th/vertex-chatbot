import streamlit as st
from db.user_repository import create_user, verify_user_credentials


def handle_sign_in():
    email = st.session_state["email"]
    password = st.session_state["password"]

    db_auth_success = verify_user_credentials(email, password)

    if db_auth_success:
        st.session_state["password_correct"] = True
        st.session_state["authenticated_email"] = email
        del st.session_state["email"]
        del st.session_state["password"]
        return

    st.session_state["password_correct"] = False


def sign_in_form(on_click):
    st.title("Chatbot Login 🤖")
    with st.form("Credentials"):
        st.text_input("Email", key="email")
        st.text_input("Password", type="password", key="password")
        st.form_submit_button("Log in", on_click=on_click)


def sign_up():
    email = st.session_state["email"]
    password = st.session_state["password"]

    user_created = create_user(email, password)

    if user_created:
        st.session_state["user_created"] = True
        st.success("User account created successfully!")
        return

    st.error("Failed to create user account. Please try again.")


def authentication_flow():
    if st.session_state.get("password_correct", False):
        if st.session_state.pop("user_created", False):
            st.success("User account created successfully!")
        return True

    sign_in_form(on_click=handle_sign_in)
    st.button("Sign Up", on_click=sign_up)

    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False
