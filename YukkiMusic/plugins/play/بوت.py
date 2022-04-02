import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")



@app.on_message(
    command(["بوت لورا"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c9a64be70b3bbca7b5dda.jpg",
        caption=f"**اسمي [{MUSIC_BOT_NAME}](https://t.me/{BOT_USERNAME}) ي وتكه شكرا لإضافتي هنا ، لتشغيل الموسيقى في المحادثه الصوتيه الخاصة بك**", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- ادخل هنا للوتاصل مع المطورين .", url=f"https://t.me/M_9_Z"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت الي مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )
