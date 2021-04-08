import asyncio
import random
import re
import time
import requests

from collections import deque

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import CMD_HELP
from userbot.system import register



dado = [
    "**È uscito:** 1 🎲",
    "**È uscito:** 2 🎲",
    "**È uscito:** 3 🎲",
    "**È uscito:** 4 🎲",
    "**È uscito:** 5 🎲",
    "**È uscito:** 6 🎲",
   
@bot.on(outgoing=True, pattern="^.dado")
async def dado(e):
    """Tira un dado!"""
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(dado))
