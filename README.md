# Aditya: AI Assistant
Aditya is made using langchain that uses Mixtral-8x7B Model using Mistral AI.

## How to run this?
1. Clone the repo
```bash
git clone https://github.com/NotoriousArnav/SimpleChatBot/
```
2. (Optional) Make a Virtual Environment for Isolation
    1.  Make the Environment
        ```bash
        python -m venv env --prompt 'Aditya'
        ```
    2. Activate it
        - Windows
            - CMD
                ```cmd
                env\Scripts\activate.bat
                ```
            - PowerShell
                ```pwsh
                env\Scripts\Activate.ps1
                ```
        - Linux/MacOS/Unix (for bash and zsh)
            ```bash
            source env/bin/activate
            ```
3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Run it
    - WebUI (ChainLit)
        ```bash
        chainlit run chainlit.py
        ```
    - CLI
        ```bash
        python cli.py -h
        ```

## LLM
The `llm.py` module purose is to make an Langchain LLM Object. Some people may prefer GPT Series of LLMs by OpenAI, or Llama or Anything Custom too. An LLM Can be Defined here, tested and can be Imported by any other module, for example `agent.py`.

### Special note for Freedom Guys and Testers
Some may even prefer Running the LLM locally or on a Private Server using Ollama, so you can totally do so, but since during development I did not have a Powerful Laptop, I did not try it, but its Reccomended, so that you can try CustomLLMs

## Tools
Currently, these are the Currently available tools.
1. scrape_article
1. Calculator
1. Stable Diffusion with Lofi Girl Adapter Image Generation
1. Stable Diffusion Image Generation
1. Studio Ghilbli Art
1. code_block
1. remember
1. starcoder2-15b
1. starcoder2-3b
1. Text Summarization
1. Wolfram Alpha Advance Calculator (Incomplete)

Tool Creation can be done using langchain's BaseTool Class.

```python
# tools/sometool.py
from langchain_communit.tools import BaseTool

class SomeTool(BaseTool): #<- Declare it Like this
    name = "Tool name"
    description = "Tool Description and Use Case"

    def _run(self, input: str) -> str:
        # Do Something
        return
```

```python
#tools/__init__.py
from .sometool import SomeTool #<- Import it
...
tools = [
    ...
    SomeTool() #<- Add that to tools list
]
...

```