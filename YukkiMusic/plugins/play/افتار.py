import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["افتار","اسكندرر","اسكندر","اسكندر","اسكندر","اسكندررر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6cee33b2fb8d85c625c2d.jpg",
        caption=f"""- مطورين سورس يورو .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- ᴜᴇsʀ ᴇᴜʀᴏ .", url=f"https://t.me/E_U_R_O_3"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ᴇᴜʀᴏ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
