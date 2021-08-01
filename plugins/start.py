import os
import time
import psutil
import shutil
import string
import asyncio
import config
from asyncio import TimeoutError
from plugins.youtube_callback_data import catch_youtube_fmtid, catch_youtube_dldata
from helper.database.access_db import db
from helper.broadcast import broadcast_handler
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client, filters, StopPropagation
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

START_TEXT = """
<b>Hello {} 👋

I'm Leo YT Downloader Bot 🇱🇰

I can download any youtube video within a short time 🙂

If you want to know how to use this bot just
touch on " Help 🆘 "  Button 😊

Leo Projects 🇱🇰</b> 
"""    
    
HELP_TEXT = """
<b>Hey {},

Please follow the below instructions to download any youtube video😊👇</b>

<code>1.Just Send Youtube Url in to this Bot..</code>
<code>2.Select The Quality and Format..</code>
<code>3.Then select Type of Your Output(Video/Doc)..</code>

<b>NOTE : Currently only support single urls.. Do not send playlists 😊</b>
"""
    
ABOUT_TEXT = """
🔰 **Bot :** [Leo YT Downloader Bot 🇱🇰](https://t.me/leoyoutubedownloaderbot)
🔰 **Developer :** [Naviya 🇱🇰🇱🇰](https://telegram.me/naviya2)
🔰 **Updates Channel :** [Leo Updates 🇱🇰](https://telegram.me/new_ehi)
🔰 **Support Group :** [Leo Support 🇱🇰](https://telegram.me/leosupportx)
🔰 **Language :** [Python3](https://python.org)
🔰 **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
🔰 **Server :** [VPS](https://www.digitalocean.com)
"""
    
INFO_TEXT = """
<b>Hey {mention},

Your details are here 😊</b>

🔰 **First Name :** `{first_name}`
🔰 **Last Name  :** `{last_name}`
🔰 **Username   :** @{username}
🔰 **User Id    :** `{user_id}`
"""
ABOUT_DEV_TEXT = """
<b>Developer is a Super Noob 😅

You can find him in telegram as @naviya2 🇱🇰

Developer's github account : [Github](https://github.com/Naviya2) 🇱🇰

If you find any error on this bot please be kind to tell [Developer](https://t.me/naviya2) or in our [Support Group](https://t.me/leosupportx) 😊</b>
"""

IMG = "https://telegra.ph/file/af76422dba43437669422.jpg"

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Developer🧑‍💻', url='https://telegram.me/naviya2'),
        InlineKeyboardButton('Rate us ★', url='https://t.me/tlgrmcbot?start=leoyoutubedownloaderbot-review')
        ],[
        InlineKeyboardButton('Updates Channel🗣', url='https://t.me/new_ehi'),
        InlineKeyboardButton('Support Group 👥', url='https://t.me/leosupportx')
        ],[
        InlineKeyboardButton('Help 🆘', callback_data='help')
        ],[
        InlineKeyboardButton('➕ Add me to your group ➕', url='https://t.me/leoyoutubedownloaderbot?startgroup=true')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About ❗️', callback_data='about'),
        InlineKeyboardButton('User Info ❗', callback_data='info')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🆘', callback_data='help'),
        InlineKeyboardButton('About Dev 🧑‍💻', callback_data='aboutdev')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    )
INFO_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About ❗️', callback_data='about'),
        InlineKeyboardButton('Help 🆘', callback_data='help')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    )
ABOUT_DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🆘', callback_data='help'),
        InlineKeyboardButton('About ❗️', callback_data='about')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    ) 


@Client.on_callback_query()
async def cb_data(client, message):
    if message.data == "home":
        await message.message.edit_text(
            text=START_TEXT.format(message.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=HELP_TEXT.format(message.from_user.mention),
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "about":
        await message.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "info":
        await message.message.edit_text(
            text=INFO_TEXT.format(username=message.from_user.username, first_name=message.from_user.first_name, last_name=message.from_user.last_name, user_id=message.from_user.id, mention=message.from_user.mention),
            reply_markup=INFO_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "aboutdev":
        await message.message.edit_text(
            text=ABOUT_DEV_TEXT,
            reply_markup=ABOUT_DEV_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "refreshme":
        if config.UPDATES_CHANNEL:
            invite_link = await client.create_chat_invite_link(int(config.UPDATES_CHANNEL))
            try:
                user = await client.get_chat_member(int(config.UPDATES_CHANNEL), message.message.chat.id)
                if user.status == "kicked":
                    await message.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/leosupportx).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.message.edit(
                    text="<b>Hey</b> {},\n\n<b>You still didn't join our Updates Channel ☹️ \nPlease Join and hit on the 'Refresh 🔄' Button</b>".format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await message.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/leosupportx).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await message.message.edit(
            text=START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS,
        )
    else:
        await message.message.delete()
        
@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return 
    await message.reply_photo(
        IMG,
        caption=START_TEXT.format(message.from_user.mention),
        reply_markup=START_BUTTONS
    )
