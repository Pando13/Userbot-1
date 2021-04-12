""" Google Translate
Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""
import asyncio
import os
import re

import requests

from userbot.Config import Config
import emoji
from googletrans import Translator
from userbot import bot
from userbot.system import dev_cmd
from asyncio import sleep
from emoji import get_emoji_regexp
from telethon import events

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
        lan = input_str or "it"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        await edit_delete(event, ".tr LanguageCode` **in risposta a messaggi**", time=5)
        return
    text = deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**Tradotto da {LANGUAGES[translated.src].title()} a {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, str(exc), time=5)
        
       
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

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)

async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None):
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in Config.SUDO_USERS:
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
