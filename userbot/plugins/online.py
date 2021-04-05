
import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd



@bot.on(dev_cmd(pattern="alive", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
 
    await event.edit(f"✅ **Userbot Online** ✅\n\n • 🗃 **Database:** `Working` \n • 🪐 **AtomicUserbot Version:** `0.66` \n • 🐍 **Python Version:** `3.9.2`\n • 📚 **Telethon Version:** `1.21.1`")

    
    

