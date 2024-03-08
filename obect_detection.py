import requests
import os
from dotenv import load_dotenv
load_dotenv()

# This uses facebook's  DETR (End-to-End Object Detection) model with ResNet-50 backbone
# This is a POC on How to Use this Model from huggingface_hub

def query(bytes_data: bytes, timeout=120):
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    headers = {
                "Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"
            }
    response = requests.post(
            API_URL,
            headers=headers,
            data=bytes_data,
            timeout=timeout
        )
    return response.json()
