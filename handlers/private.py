from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEoKT5hG4oWVSekTAie7BulSwTU92tzrQACYwMAAgHByFRdHEdhsMLgYCAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} π΅

I can play music in your group's voice chat. How's that ππΆ

Add me to your group and play music freely!β¨**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΈοΈ Developer πΈοΈ", url="https://t.me/J_A_R_V_l_S")
                  ],[
                    InlineKeyboardButton(
                        "Rhythm πΆ", url="https://t.me/RHYTHMPROBOT"
                    ),
                    InlineKeyboardButton(
                        "Sourceπ ", url="https://t.me/orthod_irunna_sankadam_varum/2"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "β Add To Your Group β", url="https://t.me/RHYTHMPROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ENQUIRY π", url="https://t.me/J_A_R_V_l_S")
                ]
            ]
        )
   )


