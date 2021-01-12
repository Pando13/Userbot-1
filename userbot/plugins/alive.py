#credits @leoatomic
import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

from datetime import datetime
from userbot.system import command

@bot.on(dev_cmd(pattern=f"on", outgoing=True))
async def amireallyalive(on):
    """ For .alive command, check if the bot is running. """
    await on.edit("**Sono online** [Capo](tg://user?id=845549379) ✔️")

@command(pattern="^.test")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**¯\_(ツ)_/¯**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("**¯\_(ツ)_/¯**\n{}".format(ms))   


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!🏓")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!🏓\n{}".format(ms))
