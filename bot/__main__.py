from pyrogram import Client, filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
from helper.forcesub import ForceSub
import config
import asyncio
import config


DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = config.BOT_TOKEN

APP_ID = config.APP_ID
API_HASH = config.API_HASH


plugins = dict(
    root="plugins",
)

Client(
    "YouTubeDlBot",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
).run()
