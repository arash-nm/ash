#!/usr/bin/env python3

import os
import sys
import readline

def run_shell():
    while True:
        # Display the prompt
        user_input = input(f"{os.getcwd()}$ ")

        # If the input is "exit", exit the shell
        if user_input.strip().lower() == "exit":
            print("Exiting shell...")
            break

        # If the input is a "cd" command, change the directory
        elif user_input.startswith("cd "):
            try:
                os.chdir(user_input[3:].strip())  # Change the directory
            except FileNotFoundError:
                print(f"Directory not found: {user_input[3:].strip()}")
        else:
            # Execute other commands
            os.system(user_input)

if __name__ == "__main__":
    run_shell()
