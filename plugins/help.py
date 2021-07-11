from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return 
    helptxt = f"<b>Currently Only Support single url(Don't Send Playlists)😶\n\n1.Just Send Youtube Url in to this Bot 🙂\n\n2.Select The Quality and Format🙂\n\n3.Then select Type of Your Out put🙂</b>"
    await message.reply_text(helptxt)
