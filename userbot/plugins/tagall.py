
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="tagall"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tagall"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()
