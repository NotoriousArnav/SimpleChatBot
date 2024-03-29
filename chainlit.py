import chainlit as cl
from agent import create_agent

agent = create_agent()

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    #TODO: Use Ollama to enable Async Token Streaming. Sadly with HF_HUB Token Streaming is not available
    out = agent.invoke(message.content)['output']
    # Send a response back to the user
    await cl.Message(
        content=out,
    ).send()

# TODO: After Each Run Dump the memory to *.memory.log.json