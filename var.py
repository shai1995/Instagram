# © Coded by @Dypixx

import os

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", ""))

CHNL_LINK = os.getenv("CHNL_LINK", "https://t.me/DypixxTech")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-100xxxxxxx"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-100xxxxxxx"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://xxxx:xxxx@xxxx")
DB_NAME = os.getenv("DB_NAME", "instalaoder")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-100xxxxxxx") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH


"""
This code is created and owned by @Dypixx. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""