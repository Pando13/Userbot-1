"""IX.IO pastebin like site
Syntax: .paste"""
from telethon import events
import asyncio
from datetime import datetime
import os
import requests
from userbot import bot
from userbot.system import dev_cmd


def progress(current, total):
    logger.info("Download {} of {}\nCompletato {}".format(current, total, (current / total) * 100))


@bot.on(dev_cmd("paste ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: .paste <long text to include>"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await bot.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: .paste <long text to include>"
    url = "https://nekobin.com/"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://nekobin.com/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://nekobin.com/v/{r['key']}"
        await event.edit("**Code copiato da {} in {} seconds. URL Originale: {}**".format(url, ms, nurl))
    else:
        await event.edit("**Code copiato da {} in {} sec**".format(url, ms))
