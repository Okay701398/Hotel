# bot/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    bot_token: str
    admin_id: int
    database_url: str

    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        self.admin_id = int(os.getenv("ADMIN_ID"))
        self.database_url = os.getenv("DATABASE_URL")

def load_config():
    return Config()
