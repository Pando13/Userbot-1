import io
import asyncio
import time
import glob
import subprocess

from telethon import events
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError

from userbot import bot
from userbot.system import dev_cmd

import os
try:
 import instantmusic , subprocess
except:
 os.system("pip install instantmusic")
 

os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    

@bot.on(dev_cmd(pattern="song ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("**Ricerca del brano...**")    
    bruh(str(cmd))
    loa = glob.glob("*.mp3")
    await event.edit("**Brano trovato**")
    await bot.send_file(
                me,
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
