import os

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")
DB = os.getenv("DB")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
