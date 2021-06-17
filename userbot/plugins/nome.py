"""Commands:
.online
.offline"""
import asyncio
import time
import random, re
import os
import shutil

from datetime import datetime
from telethon import events
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot import bot, AUTONAME, CMD_HELP
from userbot.system import dev_cmd, command

# ================= CONSTANT =================
TELEGRAM_NAME = str(AUTONAME)
# ============================================

@bot.on(dev_cmd(pattern="online"))  # pylint:disable=E0602
async def _(event):
    await event.edit(f"✅ Online⁣⁣ attivato.")
    while True:
      name = f"{TELEGRAM_NAME}⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣ [Online]⁣⁣⁣⁣"
      logger.info(name)
      await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
      
@bot.on(dev_cmd(pattern="offline"))  # pylint:disable=E0602
async def _(event):
    await event.edit(f"✅ Offline⁣⁣ attivato.")
    while True:
      name = f"{TELEGRAM_NAME}⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣ [Offline]⁣⁣⁣⁣"
      logger.info(name)
      await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
