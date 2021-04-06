from telethon import events
from userbot import bot
from userbot.system import dev_cmd
from telethon.tl.types import MessageEntityMentionName

@bot.on(dev_cmd("menziona (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        u = reply_msg.sender_id
    else:
        user, input_str = input_str.split(" ", 1)
        try:
            u = int(user)
        except ValueError:
            try:
                u = await event.client.get_entity(user)
            except ValueError:
                await event.delete()
                return
            u = int(u.id)
        except Exception:
            await event.delete()
            return
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={u}'>{input_str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )
