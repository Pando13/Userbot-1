"""Restart or Terminate the bot from any chat
Commands:
.restart
.shutdown"""
import asyncio
import os
import sys

from telethon import events
from userbot import bot, ALIVE_NAME
from userbot.system import dev_cmd

@bot.on(dev_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**Riavvio in corso...**\n**Sarò online tra 2min. prova con `.alive`**")
    await bot.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@bot.on(dev_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**Userbot spento**\n**Avviami manualmente da heroku**")
    await bot.disconnect()
