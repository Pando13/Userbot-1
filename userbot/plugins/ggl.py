from telethon import events
import os
import requests
import json
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "http://google.com/search?q={}".format(input_str.replace(" ","+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.edit("📚 **Sto cercando su Google:**\n🔎 __[{}]({})__".format(input_str, link))
    else:
        await event.edit("**Qualcosa è andato storto, riprova più tardi**")
