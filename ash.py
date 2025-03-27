#!/usr/bin/env python3

import os
import sys
import readline
from theme_loader import load_theme  # Import theme loader module

# Load the theme settings
theme = load_theme()

def run_shell():
    while True:
        # Get prompt format and apply color
        prompt = theme.get("prompt_color", "") + theme.get("prompt_format", "{cwd}$ ").format(cwd=os.getcwd()) + "\033[0m "
        
        try:
            # Display the prompt and get user input
            user_input = input(prompt)
            
            # If the input is "exit", exit the shell
            if user_input.strip().lower() == "exit":
                print("Exiting shell...")
                break
            
            # If the input is a "cd" command, change the directory
            elif user_input.startswith("cd "):
                try:
                    os.chdir(user_input[3:].strip())  # Change the directory
                except FileNotFoundError:
                    print(f"{theme.get('error_color', '')}Directory not found: {user_input[3:].strip()}\033[0m")
            else:
                # Execute other commands
                os.system(user_input)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")
        except EOFError:
            print("\nExiting shell...")
            break

if __name__ == "__main__":
    run_shell()

