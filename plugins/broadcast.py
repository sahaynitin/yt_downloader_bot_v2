#@Naviya2

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


@app.on_message(filters.private & filters.command("broadcast") & filters.user(config.BOT_OWNER) & filters.reply)
async def _broadcast(_, client: Message):
    await broadcast_handler(client)
