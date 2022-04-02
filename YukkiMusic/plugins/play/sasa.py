import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["صاصا"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f1fc1120396a35804cb61.jpg",
        caption=f"""- صاصا مبرمج سورس لورا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪ ٍ𝘿ً𝘼ٍ𝘿 ً𝙎ٍ𝘼ً𝙎ٍ𝘼 ⟫", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ʟᴜʀᴀ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
