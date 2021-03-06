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
        f"""πΌπππππππ π±ππ ππππππππ πΆππππππΔ±πππ π±ππ πππππππ πΎππππππ πΌΓΌπ£ππ Γππππππππ’ππππ. πΆπππππππ£ππ πππππ ππππππππππ πΓΌπ£ππ Γ§πππππππππ πΓ§ππ π°ππππππΔ±π ππππππππ£ππ πππππΔ± πππππππ. π°πΔ°πππ°π½; @SekerMusicAsistan.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "πΆ beni gurubuna ekleπΆ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "π KullanΔ±m KΔ±lavuzu π", url="https://t.me/mussic_kanal/135"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grubumuz ποΈ", url="https://t.me/sev_beni"
                    )],
                [
                    InlineKeyboardButton(text= "πReklam hizmetiπ", url = "https://t.me/Kalbimsin_35")
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption=f"""**π΄ {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="π΅ sahip", url=f"t.me/{OWNER}")],
                [
                    InlineKeyboardButton(
                        text="π₯ Ι’Κα΄α΄α΄", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        text="kanal π£", url=f"https://t.me/{UPDATES_CHANNEL}"
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
                InlineKeyboardButton(text="β¬οΈ ΓΆnceki", callback_data="help+5"),
                InlineKeyboardButton(text="sonraki β‘οΈ", callback_data="help+2"),
            ]
        ]
    elif pos == len(tr.HELP_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [
                InlineKeyboardButton(text="βοΈ yardΔ±m", callback_data=f"help+1"),
                InlineKeyboardButton(
                    text="gruplara ekle β",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π₯ Ι’Κα΄α΄α΄", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(
                    text="kanal π£", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ],
            [
            ],
        ]
    else:
        button = [
            [
                InlineKeyboardButton(
                    text="β¬οΈ ΓΆnceki", callback_data=f"help+{pos-1}"
                ),
                InlineKeyboardButton(
                    text="sonraki β‘οΈ", callback_data=f"help+{pos+1}"
                ),
            ],
        ]
    return button


@Client.on_message(filters.command("reload") & filters.group & ~filters.edited)
@authorized_users_only
async def admincache(client, message: Message):
    await message.reply_photo(
        photo=f"{baykaoss}",
        caption="β **Bot yeniden baΕlatΔ±ldΔ±!**\n\n **admin listesi gΓΌncellendi**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="π΅ sahip", url=f"t.me/{OWNER}")],
                [
                    InlineKeyboardButton(
                        text="π₯ Ι’Κα΄α΄α΄", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        text="kanal π£", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                ],
            ]
        ),
    )

