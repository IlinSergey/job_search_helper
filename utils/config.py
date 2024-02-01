import os

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# OpenAI
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

# YaGPT
CATALOG_ID = os.getenv("CATALOG_ID")
YA_API_KEY = os.getenv("YA_API_KEY")

MODE = os.getenv("MODE")
