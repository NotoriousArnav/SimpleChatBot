import chainlit as cl
from agent import agent

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    #TODO: Use Ollama to enable Async Token Streaming. Sadly with HF_HUB Token Streaming is not available
    out = agent.invoke(message.content)['output']
    # Send a response back to the user
    await cl.Message(
        content=out,
    ).send()