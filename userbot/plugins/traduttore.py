""" Google Translate
Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

class Config(object):
    TG_ID = os.environ.get("TG_ID", None)

from googletrans import Translator
from userbot import bot
from userbot.system import dev_cmd

from asyncio import sleep

from googletrans import LANGUAGES, Translator

from userbot import BOTLOG, BOTLOG_CHATID



@bot.on(dev_cmd("tr ?(.*)"))      
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        await edit_delete(event, "`.tl LanguageCode` as reply to a message", time=5)
        return
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**TRANSLATED from {LANGUAGES[translated.src].title()} to {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, str(exc), time=5)

async def edit_or_reply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    linktext=None,
    caption=None,
):
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096:
        parse_mode = parse_mode or "md"
        if event.sender_id in Config.TG_ID:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    asciich = ["*", "`", "_"]
    for i in asciich:
        text = re.sub(rf"\{i}", "", text)
    if aslink:
        linktext = linktext or "Message was to big so pasted to bin"
        try:
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": text}
                )
                .json()
                .get("result")
                .get("key")
            )
            text = linktext + f" [here](https://nekobin.com/{key})"
        except Exception:
            text = re.sub(r"•", ">>", text)
            kresult = requests.post(
                "https://del.dog/documents", data=text.encode("UTF-8")
            ).json()
            text = linktext + f" [here](https://del.dog/{kresult['key']})"
        if event.sender_id in Config.TG_ID:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        await event.edit(text, link_preview=link_preview)
        return event
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in Config.TG_ID:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)

        
async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None):
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in Config.TG_ID:
        reply_to = await event.get_reply_message()
        catevent = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        catevent = await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    return await catevent.delete()



async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return 
