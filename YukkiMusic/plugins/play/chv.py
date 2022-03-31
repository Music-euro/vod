import asyncio
from pyrogram import Client, filters
from staring.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(command(["اسلام"]) & filters.group & ~filters.edited)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/e0bbcfb36e9c9f196e828.jpg",
        caption=f""" تيست""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ديف", url=f"https://t.me/H_9_P")
                ]
            ]
        ),
    )
