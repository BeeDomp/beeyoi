import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
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
