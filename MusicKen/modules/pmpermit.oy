from pyrogram import Client, filters
from pyrogram.types import Message

from MusicKen.config import (
    BOT_USERNAME,
    OWNER,
    PMPERMIT,
    PROJECT_NAME,
    SUDO_USERS,
    SUPPORT_GROUP,
    UPDATES_CHANNEL,
)
from MusicKen.services.callsmusic.callsmusic import client as USER

PMSET = True
pchats = []


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE" and PMSET:
        chat_id = message.chat.id
        if chat_id in pchats:
            return
        await USER.send_message(
            message.chat.id,
            f"""**Merhaba**\n╭━━━━━━━━━━━━━━━━━╮\n┣**Assistant [{PROJECT_NAME}](https://t.me/{BOT_USERNAME})**\n**💬 GROUP  :** @{SUPPORT_GROUP}\n**👮 OWNER :** @{OWNER}\n▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰""",
            disable_web_page_preview=True,
        )
        return


@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("**Pmpermit dinyalakan**")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("**Pmpermit dimatikan**")
            return


@USER.on_message(filters.text & filters.private & filters.me)
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk Private Message")
        return
    message.continue_propagation()


@USER.on_message(filters.command("y", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk Private Message")
        return
    message.continue_propagation()


@USER.on_message(filters.command("n", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Maaf anda Ditolak untuk Private Message")
        return
    message.continue_propagation()
