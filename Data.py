from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("‹ بدء استخراج جلسة ›", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="‹ الصفحة الرأيسية ›", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✯𝐌𝐒✯ 𝒗𝒊𝒓𝒖𝒔┋✘🇨🇦!", url="https://t.me/FLASH_MASR")],
        [
            InlineKeyboardButton("‹ طريقة الاستخدام ›", callback_data="help"),
            InlineKeyboardButton("‹ حول البوت ›", callback_data="about")
        ],
        [InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗔𝗘𝗦𝗧𝗥𝗢┋✘🇨🇦!", url="https://t.me/APP_YOUTUBE")],
    ]

    START = """
━━━━━━━━🍁━━━━━━━━
⌯¦ ** مرحبـاً بـك عزيـزي ** {}
⌯¦ ** في بــوت استـخـراج جلـسـة **
⌯¦ ** استـخـراج تيرمـكـس تليثون **
⌯¦ ** وبــايــروجـرام للـمـيــوزك🎧 **
━━━━━━━━🍁━━━━━━━━
By @FLASH_MASR
    """

    HELP = """
✨ **اوامر البوت** ✨

/about - حول البوت
/help - المساعدة
/start - بدء
/generate - بدء استخراج جلسة
/cancel - 
/restart - اعادة تشغيل
"""

    # About Message
    ABOUT = """
**حول البوت** 

- بوت يقوم باستخراج جلسة تيليثون (كود تيرمكس) و جلسة بايروجرام .

[𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗔𝗘𝗦𝗧𝗥𝗢┋✘🇨🇦!](https://t.me/APP_YOUTUBE)


    """
