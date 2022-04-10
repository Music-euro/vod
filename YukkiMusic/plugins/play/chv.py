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
    async for photo in client.iter_profile_photos(BOTID, limit=1):
                    await message.reply_photo(5274610090,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘿𝙀𝙑 ¦ 𝙀𝙎𝙇𝘼𝙈", url=f"https://t.me/S_D_H_A"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ʟᴜʀᴀ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
