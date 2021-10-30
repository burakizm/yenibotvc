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
        f""" **MERHABA ARKADAŞLAR HOŞGELDİNİZ 
           Sahibim; @GOLGENDEIZIMVARR
Asistan;  @Sancakbeyasistan
Grubumuz; @sohbetsancakbeyi ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚔️ yardım", callback_data=f"help+1"),
                    InlineKeyboardButton(
                        "Gruplara ekle ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👥 ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "Kanal 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                ],
            ]
        ),
        reply_to_message_id=message.message_id,
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


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """
**🔰 Perintah**
      
**=>> Memutar Lagu 🎧**

• /oynat (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /ytplay (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /yt (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /p (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /lplay - gc'deki yanıtlanan şarkılar vcg'de otomatik olarak oynatılacaktır
• /player: Oynatıcı ayarları menüsünü açın
• /atla: Geçerli parçayı atlar
• /durdur: Parçayı duraklat
• /devam: Duraklatılan bir parçayı devam ettirir
• /son: Medya oynatmayı durdurur
• /current: Çalmakta olan parçayı görüntüler
• /playlist: Bir çalma listesi görüntüler
Komut /oynat /atla /durdur /devam /son Hariç Tüm Komutlar Yalnızca Grup Yöneticileri İçin Kullanılabilir
**==>>Şarkıyı İndir **
• /bul [şarkı adı]: youtube'dan şarkı sesini indirin      

**=>> Saluran Music Play 🛠**
      
⚪️ Hanya untuk admin channel tertaut:
      
• /cplay (nama lagu) - putar lagu yang Anda minta
• /cplaylist - Tampilkan daftar yang sedang diputar
• /cccurrent - Tampilkan sedang diputar
• /cplayer - buka panel pengaturan pemutar musik
• /cpause - jeda pemutaran lagu
• /cresume - melanjutkan pemutaran lagu
• /cskip - putar lagu berikutnya
• /cend - hentikan pemutaran musik
• /userbotjoinchannel - undang asisten ke obrolan channel Anda""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔵 sahip", url=f"t.me/By_Jilet")],
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
