import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["اسكندر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/45e8628b431b63a659299.jpg",
        caption=f"""- مبرمجين سورس يورو .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◜ ᴜᴇsʀ ᴇᴜʀᴏ ◞", url=f"https://t.me/E_U_R_O_3"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ᴇᴜʀᴏ .", callback_data=f"fft"),
                ],
            ]
        ),
    )


@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
async def khid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/81c9c970813ccfc55d3e1.jpg",
        caption=f"""انت يقلبي {message.from_user.mention()} 🙈🖤🥺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ᴇᴜʀᴏ .", url=f"https://t.me/E_U_R_O_1"),
                ],
            ]
        ),
    )
