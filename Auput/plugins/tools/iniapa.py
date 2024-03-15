import random
from pyrogram import *
from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, Message)
from config import LOG_GROUP_ID
from Auput import app as Alya


#welcome @iamuput

@Alya.on_message(filters.new_chat_members, group=3)
async def welcomek(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await Alya.get_chat_members_count(chat.id)

            welput = [
                f"{member.mention} Kambing Telah Datang!",  # Discord welcome messages copied
                f"Udah Siap Untuk Di Entod Kah Kau Badjingan? {member.mention} ?",
                f"{member.mention} Haloo Yatim. ☺",
                f"Ngapain Kau Pantek {member.mention} Join Ke Sini?",
                f"{member.mention} Aku Suka Sama Kamu, Mwahh:*!",
                f"{member.mention} Telah Hadir Untuk Ikut Live Show💦.",
                f"{member.mention} Ngapain Kesini Tod, Mau Ikut Masuk Neraka?",
                f"Halo Anak Haram {member.mention} !",
                f"{member.mention} Telah Bergabung. Semuanya, Liat Anak Anjing Ini!",
                f"Selamat Datang {member.mention}. Tetap Bertahan Yaaa.",
                f"Selamat Datang Anak Kontol, {member.mention}",
                f"Selamat Datang Anak Pantek😭 {member.mention}",
                f"Selamat Datang, {member.mention}. Keluarkan Sejanta Mu Mari Kita Perang.",
            ]
            await Alya.send_message(message.chat.id, random.choice(welput))


@Alya.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    link = await Alya.export_chat_invite_link(message.chat.id)
    for u in message.new_chat_members:
        if u.id == Alya.me.id:
            await Alya.send_message(LOG_GROUP_ID, f"""
**NEW GROUP
➖➖➖➖➖➖➖➖➖➖➖➖
NAME: {message.chat.title}
ID: {message.chat.id}
USERNAME: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖➖**
""", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"Sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))
