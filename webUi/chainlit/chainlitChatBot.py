from langserve import RemoteRunnable

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():

    runnable = RemoteRunnable("http://127.0.0.1:8000/simple/")
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: RemoteRunnable

    msg = cl.Message(content="")

    for chunk in await cl.make_async(runnable.stream)(
        {"input": message.content}
    ):
        await msg.stream_token(chunk)

    await msg.send()