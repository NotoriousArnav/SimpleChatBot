# SimpleChatBot
A Simple Chat Bot using Mixtral-8x7B Model y Mistral AI

[poc.py](poc.py) is the Original Proof of Concept Application made using the [Test Notebook](Mixtral_8x7B_test.ipynb).

A newer Approach will be taken by diving the existing Proof of Concept (POC) into smaller modules and making a Independent Application that can use any tool and is extremely modular.
For Now everything will be CLI to maintain the Simplicity.

To add a New tool, make one in the Tools folder then Import it in `tools/__init__.py` then in the tools list add the Object of Class of Tool you made and Imported.

For now Image Generation is working, in both Cases, where the API Wrapper is also Working as well as the tool call from the Agent

Note: New Tools are great but you need to add an Example Interaction in the Prompt to tell the Agent our expected output format