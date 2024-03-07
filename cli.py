from agent import agent
import argparse

parser = argparse.ArgumentParser(
    prog="aditya.cli",
    description="A Simple CLI Application to Interact with your Favorite AI Assistant",
    epilog="Thanks for Considering me - Adita and Team"
)

parser.add_argument("-p", "--prompt", help="Prompt for the Agent", required=True)
parser.add_argument("-i", "--interactive", help="If you want to Keep on Conversing with Aditya", action="store_true")
parser.add_argument("-v", "--verbose", help="If you want to look into Aditya's Thought process, or for General verbosity", action="store_true", default=False)

args = parser.parse_args()

agent.verbose = args.verbose

out = agent.invoke(args.prompt)['output']
print("Assistant", out, sep=" : ")

#TODO: Make the Program a little more CLI Friendly

if args.interactive:
    while True:
        prompt = input("Ask Aditya: ")
        out = agent.invoke(prompt)['output']
        print("Assistant", out, sep=" : ")