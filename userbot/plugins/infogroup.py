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
message_sent = 0

@bot.on(dev_cmd(pattern=("ginfo ?(.*)")))
async def _(event):
  global reply_message
   if reply_message <1:
      reply_message += 1
      return
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit(f"**Rispondi ad un utente.**")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit(f"**Rispondi ad un utente.**")
      return
   chat = "@tgscanrobot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit(f"**Rispondi ad un utente, non al bot.**")
      return
   await event.edit(f"**Ricerca info...**")
   async with bot.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1557162396))
            await bot.forward_message(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("**Sblocca** `@tgscanrobot`")
            return
         if response.text.startswith("Forward"):
            await event.edit(f"**privacy error**")
         else: 
            await event.edit(f"{response.message.message}")
