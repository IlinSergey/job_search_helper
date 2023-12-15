import os

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")
DB = os.getenv("DB")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

# YaGPT
CATALOG_ID = os.getenv("CATALOG_ID")
YA_API_KEY = os.getenv("YA_API_KEY")
