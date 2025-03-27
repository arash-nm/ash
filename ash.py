import os
import sys
import readline
import json

# تابع برای بارگذاری تم‌ها از فایل کانفیگ
def load_config():
    try:
        with open('themes.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Config file not found. Using default settings.")
        return {
            "themes": {
                "light": {
                    "prompt_color": "\\033[1;32m",  # سبز
                    "error_color": "\\033[1;31m",   # قرمز
                    "bg_color": "\\033[48;5;15m",   # سفید
                    "fg_color": "\\033[38;5;0m"     # مشکی
                }
            }
        }

def run_shell():
    # بارگذاری تنظیمات از فایل کانفیگ
    config = load_config()

    # انتخاب تم (می‌توانید از فایل کانفیگ تم دلخواه را انتخاب کنید)
    theme = config["themes"]["light"]

    # اضافه کردن /bin به اولویت جستجو برای دستورات
    os.environ["PATH"] = "/bin:" + os.environ["PATH"]
    
    while True:
        # فرمت پرامپت را با توجه به تنظیمات کانفیگ اعمال می‌کنیم
        prompt = f"{theme['prompt_color']}{os.getcwd()} > \033[0m"
        user_input = input(prompt)

        # اگر ورودی "exit" باشد، از شل خارج می‌شود
        if user_input.strip().lower() == "exit":
            print("Exiting shell...")
            break

        # اگر ورودی دستور cd باشد، دایرکتوری را تغییر می‌دهد
        elif user_input.startswith("cd "):
            try:
                os.chdir(user_input[3:].strip())  # تغییر دایرکتوری
            except FileNotFoundError:
                print(f"{theme['error_color']}Directory not found: {user_input[3:].strip()}\033[0m")
        else:
            # اجرای دستورات دیگر
            os.system(user_input)

# Entry point for the program: starts the custom shell
if __name__ == "__main__":
    run_shell()
