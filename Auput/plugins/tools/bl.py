import asyncio
import html
import re
from time import time

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import ChatPermissions, Message

from Auput import app
from Auput.misc import SUDOERS
from Auput.plugins.tools.tagall import Admin
from Auput.utils.decorators.errorrs import capture_err
from Auput.utils.decorators.admins import list_admins
from Auput.mongo.filterbl import (
    delete_blacklist_filter,
    get_blacklisted_words,
    save_blacklist_filter,
)


blacklist_filters_group = 8

__MODULE__ = "Blacklist"
__HELP__ = """
/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
"""
#chat_id = [-1001933717453]

@app.on_message(filters.command("bl",["/","!"]) & filters.group & ~filters.private)
#@adminsOnly("can_restrict_members")
async def save_filters_bl(_, message: Message):
    #chat_id = message.chat.id
    user = message.from_user
    admin_list = await list_admins(message.chat.id)
    if user.id not in admin_list:
        return
    chat_id = message.chat.id
    is_reply = True if message.reply_to_message else False
    if is_reply:
        words = message.reply_to_message.text if message.reply_to_message else message.text
    else:
        words = " ".join(message.command[1:])
    if not words:
        return await message.reply_text("Reply a message")
    if len(words) > 1:
        text = words
        to_blacklist = list(
            {trigger.strip() for trigger in text.split("\n") if trigger.strip()},
        )
        for trigger in to_blacklist:
            await save_blacklist_filter(chat_id, trigger.lower())
        #if is_reply:
            #await message.delete()
        if len(to_blacklist) == 1:
            add = await message.reply_text(
                f"Added <code>{html.escape(to_blacklist[0])}</code> to the blacklist filters!",
                parse_mode=ParseMode.HTML,
            )
        else:
            add = await message.reply_text(
                f"Added <code>{len(to_blacklist)}</code> triggers to the blacklist filters!",
                parse_mode=ParseMode.HTML,
            )
        await asyncio.sleep(1)
        await add.delete()
        await message.delete()
    else:
        await message.reply_text(
            "Usage:\n/bl [triggers] - The words/sentences you want to blacklist",
        )

@app.on_message(filters.command("cekbl",["/","!"]) & Admin & filters.group & ~filters.private)
@capture_err
async def get_filterss(_, message):
    chat_id = message.chat.id
    data = await get_blacklisted_words(chat_id)
    if not data:
        await message.reply_text("**No blacklisted words in this chat.**")
    else:
        msg = f"List of blacklisted words in {message.chat.title} :\n"
        for word in data:
            msg += f"**-** `{word}`\n"
        await message.reply_text(msg)


@app.on_message(filters.command("delbl",["/","!"]) & Admin & ~filters.private)
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/delbl [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("Usage:\n/delbl [WORD|SENTENCE]")
    chat_id = message.chat.id
    deleted = await delete_blacklist_filter(chat_id, word)
    if deleted:
        return await message.reply_text(f"**Whitelisted {word}.**")
    await message.reply_text("**No such blacklist filter.**")


@app.on_message(filters.text & filters.group & ~filters.private, group=blacklist_filters_group)
@capture_err
async def blacklist_filters_re(_, message):
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    user = message.from_user
    if not user:
        return
    if user.id in SUDOERS:
        return
    list_of_filters = await get_blacklisted_words(chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            if user.id in await list_admins(chat_id):
                return
            try:
                await message.delete()
            except Exception as e:
                print(e, "Error in blacklist filter")
                return
