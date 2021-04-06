
import datetime
import asyncio
import io
import math
import urllib.request
import os
import random
import textwrap

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker

from os import remove
from PIL import Image, ImageDraw, ImageFont

from userbot.system import register
from userbot import bot, CMD_HELP, ALIVE_NAME

@register(outgoing=True, pattern="^.ext3(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"**Rispondi a foto/sticker**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"**Rispondi a foto/sticker**")
       return
    chat = "@hazmat_suit_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"**Rispondi a un utente, non al bot.**")
       return
    await event.edit(f"**Creo Stickers...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=905164246))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Sblocca** `@hazmat_suit_bot`")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"**privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit(f"Vai su @DrWebBot e seleziona la lingua.") 
          	else: 
          			await bot.send_file(event.chat_id, response.message.media)
