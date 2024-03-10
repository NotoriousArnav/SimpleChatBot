import subprocess
import colorama
from colorama import Fore, Style

colorama.init()

print(Fore.GREEN + "Choose an option:")
print("1. Run WebUI")
print("2. Run CLI")
print("3. Run CLI with -i (interactive mode)")
print("4. Run CLI with -v (verbose mode)")
print("5. Run CLI with -i and -v" + Style.RESET_ALL)

choice = input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL)

if choice == "1":
    subprocess.run(["chainlit", "run", "chainlit.py"])
elif choice == "2":
    prompt = input(Fore.BLUE + "Enter the prompt: " + Style.RESET_ALL)
    subprocess.run(["python3", "cli.py", "-p", prompt])
elif choice == "3":
    prompt = input(Fore.BLUE + "Enter the prompt: " + Style.RESET_ALL)
    subprocess.run(["python3", "cli.py", "-p", prompt, "-i"])
elif choice == "4":
    prompt = input(Fore.BLUE + "Enter the prompt: " + Style.RESET_ALL)
    subprocess.run(["python3", "cli.py", "-p", prompt, "-v"])
elif choice == "5":
    prompt = input(Fore.BLUE + "Enter the prompt: " + Style.RESET_ALL)
    subprocess.run(["python3", "cli.py", "-p", prompt, "-i", "-v"])
else:
    print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
