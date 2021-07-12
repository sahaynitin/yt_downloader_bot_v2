import os
import time
import psutil
import shutil
import string
import asyncio
import config
from helper.broadcast import broadcast_handler
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client, filters, StopPropagation
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message



@Client.on_message(filters.command(["help"]))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return 
    helptxt = f"<u>🆘Help Menu Of Leo YT Downloader Bot🆘</u>\n\n\n<b>🔰 Currently Only Support single urls(Don't Send Playlists) 🔰\n\nJust follow the below steps to download any youtube video😊👇\n\n1.Just Send Youtube Url in to this Bot 🙂\n\n2.Select The Quality and Format🙂\n\n3.Then select Type of Your Out put🙂</b>"
    await message.reply_text(helptxt)
