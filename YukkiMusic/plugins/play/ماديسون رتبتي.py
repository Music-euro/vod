import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    command(["رتبتي"])
    & filters.user(2059448162))
async def motawer(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/02ff5eed4dc2a34cbc1f7.jpg",
        caption=f"""- ماديسون مبرمج السورس .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◜ 𝙈َ𝙖 𝘿ِ𝙞 𝙎ُ𝙤𝙉 ◞", url=f"https://t.me/MaDyY_y")
                ]
            ]
        ),
    )
