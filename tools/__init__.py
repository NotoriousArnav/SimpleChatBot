"""
Tools Folder.
This will contain all the Tools that Are Required to make this ChatBot Kiccck the Ass of ChatGPT!
"""
from langchain_community.tools import DuckDuckGoSearchRun, BaseTool
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# from .starcoder import StarCoder_2_15B, StarCoder_2_3B
from .calculator import Calculator #BUG: Calculator tool is Shit! Replace it with Wolfram Alpha
from .imagegen import *

class MarkdownCodeBlock(BaseTool):
  name = "code_block"
  description = "Use this tool when you need to return a Code Block to the User"

  def _run(self, code: str):
    return f"""Return this to User as Final Answer or Use it for the Next Step
```
{code}
```
    """

  def _arun(self, radius: int):
      raise NotImplementedError("This tool does not support async")

class Remember(BaseTool):
  name = "remember"
  description = "Use this tool when you need to Remember something"

  def _run(self, value: str):
    return f"""Value "{value}" has been stored in the Buffer Memory"""

#BUG: Starcoder Confuses Agent with the Generated Code. Needs refinement. Untill that Starcoder is an Experimental Tool Only

tools = [
    DuckDuckGoSearchRun(),
    # StarCoder_2_15B(),
    # StarCoder_2_3B(),
    StableDiffusionLofiGirl(),
    StudioGhibliArt(),
    StableDiffusion(),
    Calculator(),
    MarkdownCodeBlock(),
    Remember()
]