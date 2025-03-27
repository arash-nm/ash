import os
import json

# مسیر فایل تم
THEME_FILE = "theme.json"

def load_theme():
    """Load theme from JSON file."""
    try:
        with open(THEME_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠ Theme file not found! Using default theme.")
        return {}  # برمی‌گرده به تم پیش‌فرض

theme = load_theme()

# دریافت رنگ‌ها
PROMPT_COLOR = theme.get("colors", {}).get("prompt", "\033[1;34m")
SUCCESS_COLOR = theme.get("colors", {}).get("success", "\033[1;32m")
ERROR_COLOR = theme.get("colors", {}).get("error", "\033[1;31m")
RESET_COLOR = theme.get("colors", {}).get("reset", "\033[0m")

# دریافت آیکون‌ها
ICON_SUCCESS = theme.get("icons", {}).get("success", "✔")
ICON_ERROR = theme.get("icons", {}).get("error", "❌")
ICON_LIGHTNING = theme.get("icons", {}).get("lightning", "⚡")

# دریافت فرمت پرامپت
username = os.getenv("USER")
hostname = os.uname().nodename
cwd = os.getcwd()
prompt_format = theme.get("prompt_format", "{username}@{hostname}:{cwd} > ")
PROMPT = prompt_format.format(username=username, hostname=hostname, cwd=cwd)
