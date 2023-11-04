from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""{msg.from_user.mention},
⌯⁞ يـمكنك استـخـراج الـتـالـي
⌯⁞ تيرمـكـس تليثون للحسـابـات
⌯⁞ تيرمـكـس تليثون للبوتــات
⌯⁞بايـروجـرام مـيوزك للحسابات
⌯⁞ بايـروجـرام مـيوزك احدث اصدار
⌯⁞ بايـروجـرام مـيوزك للبوتات
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة

بواسطـة : [ٌٍALi kindi](tg://user?id=5422153027) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🌐 اضغط لبدا استخراج كود 🌐", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⚙ قناة البوت", url="https://t.me/TH3NK"),
                    InlineKeyboardButton("ALi kindi", user_id=5422153027)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
