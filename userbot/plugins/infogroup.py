@bot.on(dev_cmd(pattern=("ginfo ?(.*)")))
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
   chat = "@tgscanrobot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit(f"**Rispondi ad un utente, non al bot.**")
      return
   await event.edit(f"**Ricerca gruppi...**")
   async with bot.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
            await bot.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("**Sblocca** `@tgscanrobot`")
            return
         if response.text.startswith("Forward"):
            await event.edit(f"**privacy error**")
         else: 
            await event.edit(f"{response.message.message}")
