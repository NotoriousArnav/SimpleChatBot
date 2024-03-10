#!/usr/bin/env python3
import argparse
import colorama
import time
from agent import create_agent
import threading

colorama.init()

def cprint(text, color=colorama.Fore.WHITE, delay=0.03):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print(colorama.Style.RESET_ALL, end="", flush=True)

def print_output_thinking(text):
    cprint("Assistant : ", colorama.Fore.GREEN)
    cprint("Thinking", colorama.Fore.YELLOW, delay=0.1)
    while not output_received:  # Continue animation until output is received
        for _ in range(3):  # Simulate thinking with a simple animation
            cprint(".", colorama.Fore.YELLOW, delay=0.5)
    print()
    cprint(text, colorama.Fore.WHITE)

def output_thread_func(prompt):
    global output
    global output_received
    output = agent.invoke(prompt)['output']
    output_received = True

def print_output(text):
    cprint("Assistant : ", colorama.Fore.GREEN)
    cprint(text, colorama.Fore.WHITE)

parser = argparse.ArgumentParser(
    prog="aditya.cli",
    description="A Simple CLI Application to Interact with your Favorite AI Assistant",
    epilog="Thanks for Considering me - Aditya and Team"
)

parser.add_argument("-p", "--prompt", help="Prompt for the Agent", required=True)
parser.add_argument("-i", "--interactive", help="If you want to Keep on Conversing with Aditya", action="store_true")
parser.add_argument("-v", "--verbose", help="If you want to look into Aditya's Thought process, or for General verbosity", action="store_true", default=False)

args = parser.parse_args()

print("Making Agent", end="\r")
agent = create_agent()
print("Agent Created\r", end="\r")
# print("\r")
agent.verbose = args.verbose

output_received = False
# output_received.clear()

output_thread = threading.Thread(target=output_thread_func, args=(args.prompt,))
output_thread.start()

print_output_thinking("")  # Start the thinking animation

output_thread.join()  # Wait for the output thread to finish
print_output(output)  # Print the actual output
print()

if args.interactive:
    while True:
        try:
            prompt = input(colorama.Fore.BLUE + "Ask Aditya: " + colorama.Style.RESET_ALL)
            output_received = False
            output_thread = threading.Thread(target=output_thread_func, args=(prompt,))
            output_thread.start()  # Start the thread
            print_output_thinking("")  # Start the thinking animation
            output_thread.join()  # Wait for the output thread to finish
            print_output(output)  # Print the actual output
            print()
        except KeyboardInterrupt:
            print_output(agent.invoke('Bye')['output'])
            print()
            exit()