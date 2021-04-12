""" Google Translate
Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import emoji
from googletrans import Translator
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("tr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "it"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("`.tr LanguageCode` **in risposta a messaggi**")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**TRADUZIONE** da {} a {}
{}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))
        
       
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
