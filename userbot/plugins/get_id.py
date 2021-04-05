"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon import events
from telethon.utils import pack_bot_file_id
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("get_id"))      
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"**Utente:** `{input_str}` \n **ID:** `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"**Chat: `{p.title}`\n **ID:** `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "`Rispondi a un utente o usa l'username`")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"**Chat ID:** `{str(event.chat_id)}`\n**User ID:**` {str(r_msg.sender_id)}`\n**File ID:** `{bot_api_file_id}`",
            )
        else:
            await edit_or_reply(
                event,
                f"**Chat ID:** `{str(event.chat_id)}`\n**User ID:** `{str(r_msg.sender_id)}`",
            )
    else:
        await edit_or_reply(event, f"**Chat ID:** `{str(event.chat_id)}`")
