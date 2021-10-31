import logging

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from MusicKen.config import (
    BOT_USERNAME,
    KENKAN,
    OWNER,
    PROJECT_NAME,
    SOURCE_CODE,
    SUPPORT_GROUP,
    UPDATES_CHANNEL,
)
from MusicKen.helpers.decorators import authorized_users_only
from MusicKen.modules.msg import Messages as tr

logging.basicConfig(level=logging.INFO)


@Client.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""𝙼𝚎𝚛𝚑𝚊𝚋𝚊👋 𝙱𝚎𝚗 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙶𝚛𝚞𝚙𝚕𝚊𝚛ı𝚗𝚍𝚊 𝙱𝚊𝚗 𝚈𝚎𝚝𝚔𝚒𝚜𝚒 𝙾𝚕𝚖𝚊𝚍𝚊𝚗 𝙼ü𝚣𝚒𝚔 Ç𝚊𝚕𝚊𝚋𝚒𝚕𝚒𝚢𝚘𝚛𝚞𝚖. 𝙶𝚛𝚞𝚋𝚞𝚗𝚞𝚣𝚞𝚗 𝚜𝚎𝚜𝚕𝚒 𝚜𝚘𝚑𝚋𝚎𝚝𝚒𝚗𝚍𝚎 𝚖ü𝚣𝚒𝚔 ç𝚊𝚕𝚊𝚋𝚒𝚕𝚖𝚎𝚔 𝚒ç𝚒𝚗 𝙰𝚜𝚒𝚜𝚝𝚊𝚗ı𝚗 𝚐𝚛𝚞𝚋𝚞𝚗𝚞𝚣𝚍𝚊 𝚘𝚕𝚖𝚊𝚜ı 𝚐𝚎𝚛𝚎𝚔𝚒𝚛. 𝙰𝚂İ𝚂𝚃𝙰𝙽; @SekerMusicAsistan.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🎶 beni gurubuna ekle🎶", url="https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://t.me/mussic_kanal/135"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grubumuz 🎙️", url="https://t.me/sev_beni"
                    )],
                [
                    InlineKeyboardButton(text= "😇Reklam hizmeti😇", url = "https://t.me/Kalbimsin_35")
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption=f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔵 sahip", url=f"t.me/{OWNER}")],
                [
                    InlineKeyboardButton(
                        text="👥 ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        text="kanal 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                ],
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(["help"]))
def _help(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text=tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(map(1)),
        reply_to_message_id=message.message_id,
    )


help_callback_filter = filters.create(
    lambda _, __, query: query.data.startswith("help+")
)


@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split("+")[1])
    client.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=tr.HELP_MSG[msg],
        reply_markup=InlineKeyboardMarkup(map(msg)),
    )


def map(pos):
    if pos == 1:
        button = [
            [
                InlineKeyboardButton(text="⬅️ önceki", callback_data="help+5"),
                InlineKeyboardButton(text="sonraki ➡️", callback_data="help+2"),
            ]
        ]
    elif pos == len(tr.HELP_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [
                InlineKeyboardButton(text="⚔️ yardım", callback_data=f"help+1"),
                InlineKeyboardButton(
                    text="gruplara ekle ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="👥 ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(
                    text="kanal 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ],
            [
            ],
        ]
    else:
        button = [
            [
                InlineKeyboardButton(
                    text="⬅️ önceki", callback_data=f"help+{pos-1}"
                ),
                InlineKeyboardButton(
                    text="sonraki ➡️", callback_data=f"help+{pos+1}"
                ),
            ],
        ]
    return button


@Client.on_message(filters.command("reload") & filters.group & ~filters.edited)
@authorized_users_only
async def admincache(client, message: Message):
    await message.reply_photo(
        photo=f"{baykaoss}",
        caption="✅ **Bot yeniden başlatıldı!**\n\n **admin listesi güncellendi**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔵 sahip", url=f"t.me/{OWNER}")],
                [
                    InlineKeyboardButton(
                        text="👥 ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        text="kanal 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                ],
            ]
        ),
    )

