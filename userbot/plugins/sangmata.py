
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


@bot.on(dev_cmd(pattern=("sg ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit(f"**Rispondi ad un utente.**")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit(f"**Rispondi ad un utente.**")
      return
   chat = "@SangMataInfo_bot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit(f"**Rispondi ad un utente, non al bot.**")
      return
   await event.edit(f"**Ricerca Storico...**")
   async with bot.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
            await bot.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("**Sblocca** `@Sangmatainfo_bot`")
            return
         if response.text.startswith("Forward"):
            await event.edit(f"**privacy error**")
         else: 
            await event.edit(f"{response.message.message}")


@bot.on(dev_cmd(pattern=("gid ?(.*)")))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"**Rispondi ad un utente.**")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
       await event.edit(f"**Rispondi ad un utente.**")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"**Rispondi ad un utente, non al bot.**")
       return
    await event.edit(f"**Ricerca Info...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Sblocca** `@getidsbot`")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"**privacy error**")
          else: 
             await event.edit(f"{response.message.message}")
