from langchain_community.tools import BaseTool
import numexpr as ne

class Calculator(BaseTool):
    name = "Calculator"
    description = "Use this tool when you need to evaluate a mathematical expression. NOTE: this tool uses python numexpr library, so format your input correctly please."

    def _run(self, expression: str):
        return ne.evaluate(expression).item()

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async")
