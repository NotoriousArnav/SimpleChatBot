from langchain_community.tools import BaseTool

#TODO: To be Implemented
class WolframAlpha(BaseTool):
    name = "Wolfram Alpha Advance Calculator"
    desscription = "Use this tool, to solve Mathematical Equeations. Input should be string"

    def _run(self, problem):
        return

    def _arun(self, *args, **kwargs):
        raise NotImplementedError()