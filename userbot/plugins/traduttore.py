""" Google Translate
Commands:
.tr LanguageCode as reply to a message
"""

import os
from sys import platform
try:
    import googletrans
except:
    if platform =='linux' or platform == 'linux2':
        os.system('pip3 install googletrans')
        import aiocron
        os.system('clear')
    elif platform == 'win32':
        os.system('pip install googletrans')
        import aiocron
        os.system('cls')

import emoji
from googletrans import LANGUAGES, Translator
from userbot import bot
from userbot.system import dev_cmd

from emoji import get_emoji_regexp

from asyncio import sleep


async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result

@bot.on(dev_cmd("tr ?(.*)"))
async def _(event):
    "To translate the text."
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "it"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        await event.edit("`.tr LanguageCode` **in risposta a messaggi**")
        return
    text = deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = """📚 **Tradotto** da **__{}__** a **__{}__**:
`⁣⁣{}`⁣⁣""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)
