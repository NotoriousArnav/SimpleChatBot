"""
Tools Folder.
This will contain all the Tools that Are Required to make this ChatBot Kiccck the Ass of ChatGPT!
"""
from langchain_community.tools import DuckDuckGoSearchRun
from .starcoder import StarCoder_2_15B, StarCoder_2_3B
from .imagegen import *

tools = [
    DuckDuckGoSearchRun(),
    StarCoder_2_15B(),
    StarCoder_2_3B(),
    StableDiffusionLofiGirl(),
    StudioGhibliArt(),
    StableDiffusion()
]