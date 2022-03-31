import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["اسلام"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/ad292b6f6fbc05c824919.jpg",
        caption=f"""مبرمج سورس لورا""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘿𝙀𝙑 ¦ 𝙀𝙎𝙇𝘼𝙈", url=f"https://t.me/H_9_P")
                ]
            ]
        ),
    )
