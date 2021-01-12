#by @leoatomic
"""Commands:
.figo"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="figo", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "figo":
    await event.edit("figo")
    animation_chars = [

            "[𝙇𝙚𝙤⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣](tg://user?id=845549379) è veramente molto fiko 💪🏻 perché ha l'**Userbot**! ⚙️",
     
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])
