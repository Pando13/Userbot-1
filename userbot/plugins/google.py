import os
import time
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from re import findall
from search_engine_parser import GoogleSearch
from asyncio import sleep
from userbot.system import register
from telethon.tl.types import DocumentAttributeAudio
from . import BOTLOG, BOTLOG_CHATID
import io
import urllib
import requests

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

@register(outgoing=True, pattern=r"^\.gs (.*)")
async def gsearch(q_event):
    match = q_event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await q_event.edit(
        "**Ricerca:**\n`" + match + "`\n\n**Risultati:**\n" + msg, link_preview=False
    )
    if BOTLOG:
        await q_event.client.send_message(
            BOTLOG_CHATID,
            "Google Search query `" + match + "` was executed successfully",
        )
