import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern=("get_html ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit(f"**Rispondi ad un messaggio di un utente formattato in html.**")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit(f"**Rispondi ad un messaggio di un utente formattato in html.**")
      return
   chat = "@markuptohtmlbot"
   sender = reply_message.sender
   async with bot.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=494105609))
            await bot.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("**Sblocca** `@markuptohtmlbot`")
            return
         if response.text.startswith("Forward"):
            await event.edit(f"**privacy error**")
         else: 
            await event.edit(f"{response.message.message}")
