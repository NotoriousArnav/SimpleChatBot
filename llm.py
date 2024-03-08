# Separation of LLM and Agent is Important to Ensure a real modular approach
# Many People might just want to Run this Other LLMs might might not be present in HFHub
# So this file's purpose is to ensure that the Custom LLM is loaded properly for Inference from an source
# Any Sources mean: Ollama, OpenAI, HFHub, and etc that are supported by Langchain
from langchain_community.llms import HuggingFaceEndpoint

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.1,
    streaming=True
)