from telethon.tl.functions.messages import SaveDraftRequest


@bot.on(admin_cmd(pattern="thread$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Conto...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await event.client(
                SaveDraftRequest(
                    await event.get_input_chat(), "", reply_to_msg_id=message.id
                )
            )
        message = reply
        count += 1
    await event.edit(f"**Lunghezza del thread**: {count}")
