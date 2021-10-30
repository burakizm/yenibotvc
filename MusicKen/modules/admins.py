from asyncio.queues import QueueEmpty
from MusicKen.config import que
from MusicKen.config import BOT_USERNAME
from pyrogram import Client, filters
from pyrogram.types import Message

from MusicKen.function.admins import set
from MusicKen.helpers.channelmusic import get_chat_id
from MusicKen.helpers.decorators import authorized_users_only
from MusicKen.helpers.decorators import errors
from MusicKen.helpers.filters import command, other_filters
from MusicKen.services.callsmusic import callsmusic


@Client.on_message(filters.command(["adminreset", f"adminreset@{BOT_USERNAME}"]))
@authorized_users_only
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✅️ yönetici ön belleği yenilendi!")

@Client.on_message(command(["durdur", f"pause@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def durdur(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text(" Şeker Müsic Bot🎶❗ **şuan seste oynatılan bir music bulunamadı!**")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text(" Şeker Müsic Bot🎶▶️ **Duraklatıldı!**")


@Client.on_message(command(["devam", f"resume@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def devam(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text(" Şeker Müsic Bot🎶❗ **oynatılacak şarkı bulunamadı!**")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text(" Şeker Müsic Bot🎶⏸ **Devam ettirildi!**")


@Client.on_message(command(["son", f"end@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("Şeker Müsic Bot🎶❗ **sonlandırılacak şarkı bulunamadı!**")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("Şeker Müsic Bot🎶❌ **şarkı sonlandırıldı!**")


@Client.on_message(command(["atla", f"skip@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def atla(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("Şeker Müsic Bot🎶❗ **Atlatılanacak şarkı bulunamadı!**")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

        await message.reply_text("Şeker Müsic Bot🎶⏩ **şarkı atlatıldı!**")


@Client.on_message(filters.command(["admincache", f"admincache@{BOT_USERNAME}"]))
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✅️ **Yönetici listesi** vardır **güncellenmiş**")
