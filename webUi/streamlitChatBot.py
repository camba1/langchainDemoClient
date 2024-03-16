import streamlit as st
from langserve import RemoteRunnable

st.title("Simple Chatter")


def generate_response(prompt):
    chain = RemoteRunnable("http://127.0.0.1:8000/simple/")
    result = chain.invoke({"input": prompt})
    st.info(result)


with st.form("chat_form"):
    message = st.text_area("Enter Name of a fictional character", "Batman")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        generate_response(message)
