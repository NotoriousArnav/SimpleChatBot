from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.tools import BaseTool


class StarCoder_2_15B(BaseTool):
    name = "starcoder2-15b"
    description = """StarCoder2-15b is an AI Assistant that knows Several Programming languages.
Use this Assistant's Help to Generate Code.
This is assistant is Trained on 15 Billion parameters
Beware: This Tool can sometimes generate code that might not be correct or repetative, so you need to verify that before you return this to user
    """
    llm = HuggingFaceEndpoint(repo_id="bigcode/starcoder2-3b")

    def _run(self, prompt: str) -> str:
        return self.llm.invoke(prompt)

    def _arun(self, prompt: str) -> str:
        raise NotImplementedError()

class StarCoder_2_3B(BaseTool):
    name = "starcoder2-3b"
    description = """StarCoder2-3b is an AI Assistant that knows Several Programming languages.
Use this Assistant's Help to Generate Code.
This is assistant is Trained on 3 Billion parameters
Beware: This Tool can sometimes generate code that might not be correct or repetative, so you need to verify that before you return this to user
    """
    llm = HuggingFaceEndpoint(repo_id="bigcode/starcoder2-3b")

    def _run(self, prompt: str, **kwargs) -> str:
        return self.llm.invoke(prompt)

    def _arun(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError()
