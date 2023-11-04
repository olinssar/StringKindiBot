from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://alikindi.online/quranjpg/nizk.jpg", caption=f"» 📣 لا يمكنك استخدام البوت . [ٍ꙳𝗌𝗈𝗎𝗋𝖼𝖾 𝗇𝗂𝗓𝗄({link}) 🔘 الا بعد الاشتراك بقناة البوت . [𝗌𝗈𝗎𝗋𝖼𝖾 𝗇𝗂𝗓𝗄]({link}) 📡 اشترك بقناة بعدها ارسل /start .",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("꙳𝗌𝗈𝗎𝗋𝖼𝖾 𝗇𝗂𝗓𝗄", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
