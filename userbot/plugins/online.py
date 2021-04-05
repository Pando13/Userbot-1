import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="alive", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    uptime = await get_readable_time((time.time() - StartTime))
    await event.edit(f"✅ **Userbot Online** ✅\n\n • 🗃 **Database:** `Working` \n • 🪐 **AtomicUserbot Version:** `4.6` \n • 🐍 **Python Version:** `3.9.2` \n • 📚 **Telethon Version:** `1.21.1` \n • ⏳ **UpTime:** `{uptime}\n ")

    
    
    async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time
