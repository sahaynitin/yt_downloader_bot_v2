#@Naviya2

import config
from helper.broadcast import broadcast_handler
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.private & filters.command("broadcast") & filters.user(config.BOT_OWNER) & filters.reply)
async def broadcast(_, m: Message):
    await broadcast_handler(m)
