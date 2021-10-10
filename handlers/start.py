from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/e775aff9d6a97c5664d65.jpg")
    await message.reply_text(
        f"""**Hey, I'm 『PRINCE MUSIC』 MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [『PRINCE✰』](https://t.me/Princepati96k)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝐔𝐏𝐃𝐀𝐓𝐄𝐃𝐒♐", url="https://t.me/KING_PRINCE_SUPPORT")
                  ],[
                    InlineKeyboardButton(
                        "📢 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 📢", url="https://t.me/STUDY_FLOWER_QUIZ_GROUP"
                    
                    InlineKeyboardButton(
                        "👑𝐎𝐖𝐍𝐄𝐑👑", url="https://t.me/Princepatil96k"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏", url="https://t.me/PRINCE_KING_MUSIC?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**『PRINCE PATIL』 IS ALIVE**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🔰", url="https://t.me/KING_PRINCE_SUPPORT")
                ]
            ]
        )
   )


