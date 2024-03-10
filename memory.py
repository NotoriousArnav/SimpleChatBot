# Memory and Related Tools will be Defined here
from langchain.memory import ConversationBufferWindowMemory

# TODO: Add a Function to Dump and Restore memory to/from JSON 
# TODO: Add a Function to Summarize Memory and Dump in *.memory.summary.log

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=11,
    return_messages=True,
)