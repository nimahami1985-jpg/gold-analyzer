import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# -----------------------------
# تنظیمات
# -----------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TGJU_URL = "https://www.tgju.org/profile/geram18"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
    )
}
