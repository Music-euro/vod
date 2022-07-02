import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["قناة السورس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/45e8628b431b63a659299.jpg",
        caption=f"""- قناة سورس يورو الرسميه .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضغط هنا لدخول القناة .", url=f"https://t.me/E_U_R_O_1"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ᴇᴜʀᴏ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
