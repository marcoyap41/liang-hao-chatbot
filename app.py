import chainlit as cl
from ollama import AsyncClient

MODEL_NAME = "deepseek-r1:1.5b"


@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "interaction",
        [
            {
                "role": "system",
                "content": "You are a helpful AI assistant named Liang Hao.",
            }
        ],
    )

    msg = cl.Message(content="")
    start_message = "Hello, I am Liang Hao. An artificial intelligence running in your local machine. How can I help you today?"

    for char in start_message:
        await msg.stream_token(char)

    await msg.send()


@cl.on_message
async def main(message: cl.Message):
    interaction = cl.user_session.get("interaction")
    interaction.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    client = AsyncClient()
    response_stream = await client.chat(
        model=MODEL_NAME,
        messages=interaction,
        stream=True,
    )

    full_response = ""
    async for chunk in response_stream:
        token = chunk.message.content
        if token:
            full_response += token
            await msg.stream_token(token)

    interaction.append({"role": "assistant", "content": full_response})
    await msg.update()
