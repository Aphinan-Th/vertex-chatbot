import streamlit as st
from db.user_repository import get_user_by_email
from vertexai.generative_models import FunctionDeclaration, GenerativeModel, Tool


def attach_message(content: str, role: str = "user") -> dict:
    return {"role": role, "content": content}


def init_chat_history() -> None:
    if "messages" not in st.session_state:
        st.session_state["messages"] = []


def display_messages() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def create_tool(name: str, description: str, parameters: dict) -> Tool:
    function_declaration = FunctionDeclaration(
        name=name,
        description=description,
        parameters=parameters,
    )
    return Tool(function_declarations=[function_declaration])


def create_user_details_tool() -> Tool:
    parameters = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "age": {"type": "string"},
            "address": {"type": "string"},
        },
        "required": ["email"],
    }
    return create_tool("get_user_details", "Get user details", parameters)


def process_get_user_details(params: dict, authenticated_email: str) -> str:
    if params["email"] != authenticated_email:
        return "Error: You can only access your own details."
    user = get_user_by_email(params["email"])
    return f"Name: {user.name}\nEmail: {user.email}\nAge: {user.age}\nAddress: {user.address}"


def process_function_call(function_call, authenticated_email: str) -> str:
    if not function_call:
        return ""

    if function_call.name == "get_user_details":
        params = {key: value for key, value in function_call.args.items()}
        return process_get_user_details(params, authenticated_email)

    return "Error: Unsupported function call."


def handle_user_input(model: GenerativeModel) -> None:
    user_details_tool = create_user_details_tool()
    prompt = st.chat_input("Type your message here...")
    if not prompt:
        return

    user_message = attach_message(prompt)
    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.write(prompt)

    chat_session = model.start_chat()
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        auth_email = st.session_state.get("authenticated_email")

        for chunk in chat_session.send_message(
            prompt,
            stream=True,
            tools=[user_details_tool],
        ):
            parts = chunk.candidates[0].content.parts[0]
            function_call = getattr(parts, "function_call", None)

            if function_call:
                response = process_function_call(function_call, auth_email)
            else:
                response = parts.text

            full_response += response
            response_placeholder.markdown(full_response)

        response_placeholder.markdown(full_response)
        assistant_message = attach_message(full_response, "assistant")
        st.session_state.messages.append(assistant_message)
