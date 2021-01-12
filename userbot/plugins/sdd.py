"""" Spotify / Deezer downloader plugin by @leo4tomic | Syntax: .sdd link"""
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.system import dev_cmd

@bot.on(dev_cmd("sdd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("🎶**Sto iniziando a scaricare!**🎶")
    bot = "@DeezLoadBot"
    
    async with borg.conversation("@DeezLoadBot") as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              try:
                  await bot(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
              except UserAlreadyParticipantError:
                  await asyncio.sleep(0.00000069420)
              await conv.send_message(d_link)
              details = await conv.get_response()
              await bot.send_message(event.chat_id, details)
              await conv.get_response()
              songh = await conv.get_response()
              await bot.send_file(event.chat_id, songh, caption="🔆**Ecco la canzone richiesta**🔆")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
