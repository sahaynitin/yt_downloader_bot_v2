from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel🗣", url="https://t.me/new_ehi")],
        [InlineKeyboardButton(
            "Developer🧑‍💻", url="https://t.me/naviya2")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}👋\n\nYou are Warmly welcome to Leo YT Downloader Bot🇱🇰</b>\n\nIf you want to know how i works just touch on /help command🙂\n\n\nMade By : @naviya2 🇱🇰\nSupport Group : @leosupportx🇱🇰"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
