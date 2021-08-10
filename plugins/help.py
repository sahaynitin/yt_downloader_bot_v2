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

HELP_ANIMATION = "https://telegra.ph/file/0b0d158e6523ad7962b7e.mp4"

@Client.on_message(filters.command(["help"]))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await message.reply_animation(
        HELP_ANIMATION,
        caption="Hey {},\n\nPlease follow the below instructions to download any youtube video😊👇\n\n<code>1.Just Send Youtube Url in to this Bot..(You can search inline and get yt link in this bot 🙃 to do that, simply type bot's user name in your type bar and type the name of your video)</code>\n\n<code>2.Select The Quality and Format..</code>\n\n<code>3.Then select Type of Your Output(Video/Doc)..</code>\n\n<b>Note : Currently only support single urls.. Do not send playlists 😊</b>\n\n<b>You can watch our video tutorial by the below button</b>".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
            
                InlineKeyboardButton("Tutuorial Video 💫", url="https://t.me/new_ehi/353")
             
            ],
        ),
    )
   
