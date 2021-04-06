#credits @leoatomic
import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

from datetime import datetime
from userbot.system import command

@bot.on(dev_cmd(pattern="alive", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit(f"ㅤ  [✅](tg://user?id=845549379) **Userbot Online** \n\n **《 🗃 Database:** `Working` \n **《 🪐 AtomicUserbot Version:** `1.0` \n **《 🐍 Python Version:** `3.9.2`\n **《 📚 Telethon Version:** `1.21.1` \n **《 📶 Ping:** `Calcolo...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"ㅤ  [✅](tg://user?id=845549379) **Userbot Online** \n\n **《 🗃 Database:** `Working` \n **《 🪐 AtomicUserbot Version:** `1.0` \n **《 🐍 Python Version:** `3.9.2`\n **《 📚 Telethon Version:** `1.21.1` \n **《 📶 Ping:** `{ms}`")

@bot.on(dev_cmd(pattern=f"on", outgoing=True))
async def amireallyalive(on):
    """ For .alive command, check if the bot is running. """
    await on.edit("**Online** [✔️](tg://user?id=845549379)")

@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!🏓")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!🏓\n{}".format(ms))
