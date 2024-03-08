from langchain_community.tools import BaseTool
import requests
import os

from dotenv import load_dotenv
load_dotenv()

class text_summarization(BaseTool):
    name="Text Summarization"
    description = "Use this tool to Summurize Large text."

    def query(self, payload):
        API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
        headers = {
                "Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"HUGGINGFACEHUB_API_TOKEN
            }
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    def _run(self, text: str) -> str:
        data = self.query({"inputs": text})
        return data[0]['summary_text']
        
