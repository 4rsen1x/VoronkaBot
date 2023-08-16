import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
dotenv_path = Path(BASE_DIR / "config.env")
DB_PATH = Path(BASE_DIR / "users.db")
# admins = [734609007, 693071364]
load_dotenv(dotenv_path=dotenv_path)
BOT_KEY = os.getenv("BOT_KEY")
ANDROID_LINK = os.getenv("ANDROID_LINK")
IOS_LINK = os.getenv("IOS_LINK")
LANDING_LINK = os.getenv("LANDING_LINK")
KOPILKA_LINK = os.getenv("KOPILKA_LINK")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
STICKER_ID = os.getenv("STICKER_ID")
GROUP_ID = int(os.getenv("GROUP_ID"))
