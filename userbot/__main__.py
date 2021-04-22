
import aiocron, asyncio

from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.system import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils
import heroku3

import time
import random, re
import os
import shutil

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon import events
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot import bot, AUTONAME, DEFAULT_BIO, CMD_HELP
from userbot.system import dev_cmd, command

# ================= CONSTANT =================
DEFAULTUSERBIO = str(DEFAULT_BIO) if DEFAULT_BIO else "ᗯᗩᏆᎢᏆᑎᏀ ᏞᏆᏦᗴ ᎢᏆᗰᗴ"
DEL_TIME_OUT = 60


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Avvio Bot Inline")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Avvio Bot Inline completato senza errori")
        print("Avvio Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        if Var.HEROKU_APP_NAME and Var.HEROKU_API_KEY is not None:
            Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
            app = Heroku.app(Var.HEROKU_APP_NAME)
            heroku_var = app.config()
            variable = "SUDO_USERS"
            if variable in heroku_var:
                del heroku_var[variable]
            else:
                print("Avvio Userbot completato senza errori")
        print("Avvio terminato")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print("AtomicUserbot in esecuzione, test con .alive")



@aiocron.crontab('*/1 * * * *')
async def set_clock():
    DMY = time.strftime("%d/%m/%Y")
    HM = time.strftime("%H:%M")
    bio = f"⌚️ {HM} | {DEFAULTUSERBIO} | {DMY} 🗓"
    try:
        await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
    except FloodWaitError as ex:
        logger.warning(str(e))
        await asyncio.sleep(ex.seconds)        
        
        
        
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.loop.create_task(set_clock())
    bot.run_until_disconnected()
