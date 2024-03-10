# Separation of LLM and Agent is Important to Ensure a real modular approach
# Many People might just want to Run this Other LLMs might might not be present in HFHub
# So this file's purpose is to ensure that the Custom LLM is loaded properly for Inference from an source
# Any Sources mean: Ollama, OpenAI, HFHub, and etc that are supported by Langchain
import os
from contextlib import redirect_stdout, redirect_stderr
from langchain_community.llms import HuggingFaceEndpoint

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

with open(os.devnull, 'w') as null_file:
    with redirect_stdout(null_file), redirect_stderr(null_file):
        llm = HuggingFaceEndpoint(
            repo_id=repo_id,
            temperature=0.5,
            # streaming=True,
        )
