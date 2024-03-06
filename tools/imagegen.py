from langchain_community.tools import BaseTool
# from PIL import Image
import requests
import os
import io

class StableDiffusionLofiGirl(BaseTool):
    name = "Stable Diffusion with Lofi Girl Adapter Image Generation"
    description = "Generate images using the Stable Diffusion model with the Lofi Girl adapter and upload them to 0x0.st. Returns the URL of the uploaded image."

    def _run(self, prompt: str) -> str:
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        api_url = "https://api-inference.huggingface.co/models/Norod78/SDXL-LofiGirl-Lora"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        image_bytes = response.content

        upload_url = "https://0x0.st/"
        files = {'file': image_bytes}
        upload_response = requests.post(upload_url, files=files, timeout=120)
        uploaded_image_url = upload_response.text.strip()

        return uploaded_image_url

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError()

class StableDiffusion(BaseTool):
    name = "Stable Diffusion Image Generation"
    description = "Generate images using the Stable Diffusion model and upload them to 0x0.st. Returns the URL of the uploaded image."

    def _run(self, prompt: str) -> str:
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        image_bytes = response.content

        upload_url = "https://0x0.st/"
        files = {'file': image_bytes}
        upload_response = requests.post(upload_url, files=files, timeout=120)
        uploaded_image_url = upload_response.text.strip()

        return uploaded_image_url

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError()

class StudioGhibliArt(BaseTool):
    name = "Studio Ghilbli Art"
    description = "Image Generation using Stable Diffusion. Uses a LoRa that produces the Output in Studio Ghibli Art Style. Returns an Image URL"

    def _run(self, prompt:str) -> str:
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        API_URL = "https://api-inference.huggingface.co/models/KappaNeuro/studio-ghibli-style"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
                API_URL,
                headers=headers,
                json={
                    "inputs": f"Studio Ghibli Style -{prompt}.Studio Ghibli Cel Style"
                },
                timeout=120
            )
        data = io.BytesIO(response.content)
        response = requests.post(
                'https://0x0.st/',
                files={'file':data},
                timeout = 120
            )
        return str(response.text.strip())

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError()

#TODO: Add Other Loras. Refer: https://huggingface.co/spaces/multimodalart/LoraTheExplorer
    