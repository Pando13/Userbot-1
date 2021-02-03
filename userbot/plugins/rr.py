import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="rr", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "rr":
    await event.edit("rr")
    animation_chars = [

            "🌐 Clicca ➡️ [QUI](https://bit.ly/2NT29jC) ⬅️ per visualizzare il risultato della ricerca 🔎",
     
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])
