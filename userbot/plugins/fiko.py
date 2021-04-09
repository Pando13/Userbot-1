#SOLO PER @leoatomic
"""Commands:
.fika"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="fika", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("[𝙇𝙚𝙤⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣](tg://user?id=845549379) è veramente molto fiko 🦾 perché ha **creato @AtomicUserbot**! 🪐")
