import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
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
    command(["start"])
    & filters.group
    & ~filters.edited
)
@LanguageStart
async def hilo(client, message: Message, _):
    out = start_pannel(_)
    await message.reply_photo(
        photo=f"https://telegra.ph//file/ad292b6f6fbc05c824919.jpg",
        caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاعدادات", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "الاوامر", url=f"https://t.me/{app.username}?start=help")
                ],[
                    InlineKeyboardButton(
                        text=_["PL_B_12"], url=f"https://t.me/so_alfaa"),
            ],
            ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("eslam"))
async def eslam(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""jkgkyjhuu""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "الاعدادات", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "الاوامر", url=f"https://t.me/{app.username}?start=help")
                ],[
                    InlineKeyboardButton(
                        text=_["PL_B_12"], url=f"https://t.me/so_alfaa"),
            ],
            ]
        ),
    )
