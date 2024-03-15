import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from blackpink import blackpink as bp
from Auput import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@app.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink ") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png")
    await message.reply_photo(f"blackpink_{message.from_user.id}.png")
    os.remove(f"blackpink_{message.from_user.id}.png")


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git iamuput")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""Github Info Of {name}
                
**Username**: {username}
**Bio**: {bio}
**Company**: {company}
**Created on**: {created_at}
**Repositories**: {repositories}
**Blog**: {blog}
**Location**: {location}
*Followers**: {followers}
**Following**: {following}"""

            except Exception as e:
                print(str(e))
                pass

    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="Link", url=f"{url}"
            ),
            InlineKeyboardButton(
                text="Close", callback_data="close"
            )
               ],
            ]
    )
                             )
