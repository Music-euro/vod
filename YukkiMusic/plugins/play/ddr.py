import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)



@app.on_message(
    command(["سورس يورو","يورو"])
    & filters.group
    & ~filters.edited
)
@LanguageStart
async def hilo(client, message: Message, _):
    out = start_pannel(_)
    await message.reply_video(
        video=f"https://telegra.ph/file/e68decfeef29a9f1f8c80.mp4",
        caption=f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐄𝐔𝐑𝐎 .](https://t.me/E_U_R_O_1)\n\n[❍ | 𝐄𝐔𝐑𝐎 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/E_U_R_O_1)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/E_U_R_O_1)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاعدادات", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "الاوامر", url=f"https://t.me/{app.username}?start=help")
                ],[
                    InlineKeyboardButton(
                        "مطورين السورس", callback_data=f"eslam"),
            ],
            ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("eslam"))
async def eslam(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""- للتواصل مع مطورين سورس يورو اتبع الازرار .""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "- مبرمجين السورس .", url=f"https://t.me/E_U_R_O_3"),
                    InlineKeyboardButton(
                        "- المبرمج اسكندر .", url=f"https://t.me/DAD_A_S_K_A_N_D_E_R")
                ],[
                    InlineKeyboardButton(
                        "قناه السورس", url=f"https://t.me/E_U_R_O_1"),
                ],[
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
                    InlineKeyboardButton(
                        "رجوع", callback_data="back11"),
               ],
          ]
        ),
    )

    
