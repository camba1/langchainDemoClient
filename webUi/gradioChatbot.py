import gradio as gr
from langserve import RemoteRunnable


def predict(prompt, history):
    chain = RemoteRunnable("http://127.0.0.1:8000/simple/")
    # gpt_response = chain.invoke({"input": prompt})
    # return gpt_response
    partial_message = ""
    for chunk in chain.stream({"input": prompt}):
        partial_message = partial_message + chunk
        yield partial_message


gr.ChatInterface(predict).launch()

