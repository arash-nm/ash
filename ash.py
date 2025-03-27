import os
import sys

def run_shell():
    while True:
        # نمایش پرامپت
        user_input = input(f"{os.getcwd()}$ ")

        # اگر ورودی "exit" باشد، از شل خارج می‌شود
        if user_input.strip().lower() == "exit":
            print("Exiting shell...")
            break

        # اگر ورودی دستور shell باشد، آن را اجرا می‌کند
        elif user_input.startswith("cd "):
            try:
                os.chdir(user_input[3:].strip())  # تغییر دایرکتوری
            except FileNotFoundError:
                print(f"Directory not found: {user_input[3:].strip()}")
        else:
            # اجرای دستورات دیگر
            os.system(user_input)

if __name__ == "__main__":
    run_shell()
