# by @leo4tomic

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "stacca":

        await event.edit(input_str)

        animation_chars = [

           "Attenzione è entrato un disturbo" ,
           "L'output è sospeso... " ,
           "Attento...!" ,
           "Forse ci stanno tracciando..." ,
           "Ci stanno TRACCIANDO!!!" ,
           "STACCA!" ,
           "STACCA!!" ,
           "STACCA!!!..." ,
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
