from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup, Message
from helper.forcesub import ForceSub
import asyncio
import config


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return 
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer🧑‍💻", url="https://t.me/naviya2"),
        InlineKeyboardButton("Rate us ★", url="https://t.me/tlgrmcbot?start=leoyoutubedownloaderbot-review")],
        
        [InlineKeyboardButton("Updates Channel 🗣", url="https://t.me/new_ehi"),
        InlineKeyboardButton("Support Group 👥", url="https://t.me/leosupportx")],
        
        [InlineKeyboardButton("➕ Add me to your group ➕", url="https://t.me/leoyoutubedownloaderbot?startgroup=true")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}👋\n\nYou are Warmly welcome to Leo YT Downloader Bot 🇱🇰</b>\n\nIf you want to know how i works just touch on /help command 🙂"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
