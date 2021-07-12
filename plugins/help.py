from pyrogram import Client, filters, StopPropagation
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
import config


@Client.on_message(filters.command(["help"]))
async def start(client, message):
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return 
    helptxt = f"<b>Currently Only Support single url(Don't Send Playlists)😶\n\n1.Just Send Youtube Url in to this Bot 🙂\n\n2.Select The Quality and Format🙂\n\n3.Then select Type of Your Out put🙂</b>"
    await message.reply_text(helptxt)
