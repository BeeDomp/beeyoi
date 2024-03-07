import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOG_GROUP_ID
from Auput import app  

uputlogo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 Mᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(uputlogo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"Sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "Unknown Users"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "Private Chats"
        chat_id = message.chat.id
        left = f"✫ <b><u>#Left_Group</u></b> ✫\n\nChat Tittle : {title}\n\nChat ID : {chat_id}\n\nRemoved By : {remove_by}\n\nBot : @{app.mention}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(uputlogo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🌷Welcome in a New Group🥳\n\n"
                f"📌Chat Name: {message.chat.title}\n"
                f"🔐Chat Username: @{message.chat.username}\n"
                f"✍️Ur Username: @{member.username}\n"
                f"👥Group {count} Members🎉"
            )
            await app.send_photo(message.chat.id, photo=random.choice(uputlogo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"Culik akuuuu><", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
