import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["حمودي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2cae08ee50c635af5baeb.jpg",
        caption=f"""- حمودي مبرمج سورس لورا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪ ٍ𝘏 𝘈 𝘔 𝘖 𝘋 𝘠 ⟫", url=f"https://t.me/PV_HM9DY"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ᴇᴜʀᴏ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
