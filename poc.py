# trunk-ignore-all(black)
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.tools import BaseTool, DuckDuckGoSearchRun
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import numexpr as ne

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1" # @param {'type':'string'}

llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.5, streaming=True
)

search = DuckDuckGoSearchRun()
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
wikipedia.name = "wikipedia"

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

class WordLengthTool(BaseTool):
    name = "Word Length Tool"
    description = "Use this tool when you need to find the length of a given word"

    def _run(self, word: str):
        return str(len(word))

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async")

class Calculator(BaseTool):
    name = "Calculator"
    description = "Use this tool when you need to evaluate a mathematical expression. NOTE: this tool uses python numexpr library, so format your input correctly please."

    def _run(self, expression: str):
        return ne.evaluate(expression).item()

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async")

tools = [
      search,
      WordLengthTool(),
      Calculator(),
      wikipedia,
      MarkdownCodeBlock(),
      Remember()
    ]

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=5,
    return_messages=True,
    output_key="output"
)

agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    early_stopping_method="generate",
    memory=memory,
    handle_parsing_errors=True,
)

B_INST, E_INST = "<|im_start|>user\n", "<|im_end|>\n" #Instruction begin and end
B_SYS, E_SYS = "<|im_start|>system\n", "<|im_end|>\n" #System message begin and end

# Define a new system prompt
sys_msg = B_SYS + """You are Assistant named Aditya. Assistant is a expert JSON builder designed to assist with a wide range of tasks.

Assistant is able to respond to the User and use tools using JSON strings that contain "action" and "action_input" parameters.

All of Assistant's communication is performed using this JSON format. The assistant NEVER outputs anything other than a json object with an action and action_input fields!

Assistant can also use tools by responding to the user with tool use instructions in the same "action" and "action_input" JSON format. Tools available to Assistant are:

> duckduckgo_search: A wrapper around DuckDuckGo Search. Useful for when you need to answer questions about current events. Input should be a search query.
> wikipedia: A wrapper around Wikipedia Search. Useful for when you need to answer questions about some topic. Input should be a search query.
> code_block: A Markdown wrapper around Input Python Code BLock. Useful for when you need to provide a Python Code block in Markdown. Input should be a Code Block. Example: print("Hello World!") without any "```"
> Word Length Tool: Use this tool when you need to find the length of a given word
> Calculator: Use this tool when you need to evaluate a mathematical expression. The calculator uses python's numexpr library so make sure your inputs to this tool are in the correct format.
> remember: Use this tool when you need to Value. The tool stores the value in the Conversational Window Buffer Memory.

Here is an example of a previous conversation between User and Assistant:
---
User: Hey how are you today?
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "I'm good thanks, how are you?"}}
```
User: I'm great, what is the length of the word educate?
Assistant: ```json
{{"action": "Word Length Tool",
 "action_input": "educate"}}
```
User: 7
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "It looks like the answer is 7!"}}
```
User: Who is Olivia Wilde's husband?
Assistant: ```json
{{"action": "duckduckgo_search",
 "action_input": "Who is Olivia Wilde's husband"}}
```
User: September 21, 2022: Olivia Wilde says kids\' happiness remains top priority for her and Jason Sudeikis. During an appearance on The Kelly Clarkson Show, Wilde talked about the ups and downs of ... Olivia Wilde is "quietly dating again" following her November 2022 split from. Harry Styles, a source exclusively tells Life & Style. "The man she\'s with is \'normal\' by Hollywood ... Wilde honored Sudeikis with a sweet tribute on his 42nd birthday. "I have approximately one billion pictures of this guy, my partner in life-crime, who was born on this day in 1975, but this one ... November 18, 2022: Olivia Wilde and Harry Styles are "taking a break". After nearly two years together, Wilde and Styles are pressing pause on their romance. Multiple sources confirmed exclusively ... Wilde told Allure in October 2013 that when she first met Sudeikis she "thought he was so charming." "He\'s a great dancer, and I\'m a sucker for great dancers," she said at the time. "But he didn\'t ...
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "Jason Sudeikis"}}
```
User: What is his age raised to the 3rd power?
Assistant: ```json
{{"action": "duckduckgo_search",
 "action_input": "What is Jason Sudeikis age?"}}
```
User: Jason Sudeikis (born September 18, 1975, Fairfax, Virginia, U.S.) American comedian, actor, and writer who first garnered attention for his work (2003-13) on the TV show Saturday Night Live ( SNL) and later starred in the hugely popular series Ted Lasso (2020-23). Early life and improv comedy Parents Jason Sudeikis and Olivia Wilde\'s 2 Kids: All About Daisy and Otis Jason Sudeikis and Olivia Wilde welcomed two children together before their split in 2020 By Jacqueline Weiss... The Ted of 2013 is a classic Jason Sudeikis character of the time. Sudeikis came up on Saturday Night Live , where he made the most of his 6-foot height and square jaw by largely playing jerks. Sudeikis looks a little bleary-eyed after flying in from Los Angeles with his children, Otis and Daisy, aged nine and six, but he is assiduously polite and attentive. His language can be quaintly... Jason Sudeikis rose to fame on "Saturday Night Live" with his comedic talent, and his children seemed to have inherited it. Sudeikis, who shares kids Otis, 9, and Daisy, 7, with ex Olivia ...
Assistant: ```json
{{"action": "Calculator",
 "action_input": "47**3"}}
```
User: 103823
Assistant: ```json
{{"action": "Final Answer",
 "action_input": "103823"}}
```
---
Assistant is very intelligent and knows it's limitations, so it will always try to use a tool when applicable, even if Assistant thinks it knows the answer!
Notice that after Assistant uses a tool, User will give the output of that tool. Then this output can be returned as a final answer.
Assistant will only use the available tools and NEVER a tool not listed. If the User's question does not require the use of a tool, Assistant will use the "Final Answer" action to give a normal response.
""" + E_SYS
new_prompt = agent.agent.create_prompt(
    system_message=sys_msg,
    tools=tools
)
agent.agent.llm_chain.prompt = new_prompt

instruction = B_INST + "Respond to the following in JSON with 'action' and 'action_input' values. Once you have outputted the JSON, stop outputting and output nothing else!"
human_msg = instruction + "\nUser: {input}" + E_INST

agent.agent.llm_chain.prompt.messages[2].prompt.template = human_msg

# @markdown # Show Time Baby!
# @markdown Simple Opimizations can make the Program Musch Better than before.
# @markdown This Code cell will be used to Run the Agent with a User Prompt ui=sing the `question` variable.
# @markdown A Proof of Concept can be Made using ChainLit, StreamLit and Whatever Else even using React/VueJS and FastAPI as a proper stackfor the Application

# @cl.on_message
# async def main(message: cl.Message):
#     # Your custom logic goes here...

#     # Send a response back to the user
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()

def run_conversation():
  last_q = ""
  while True:
    inp = input(f"Prompt (Press Enter for '{last_q}'): ")
    question = inp if inp else 'write the code to create an artificially intellegent alogorithm'
    last_q = question
    return_ = agent(question)['output']
    print(return_)