#SOLO PER @leoatomic
"""Commands:
.fika"""

import asyncio
from telethon import events
from userbot import TG_ID, AUTONAME, bot
from userbot.system import dev_cmd


# ================= CONSTANT =================
TELEGRAM_ID = str(TG_ID)
TELEGRAM_NAME = str(AUTONAME)
# ============================================

@bot.on(dev_cmd(pattern="fika", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"[{TELEGRAM_NAME}⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣](tg://user?id={TELEGRAM_ID}) è veramente molto fiko 🦾 perché ha **AtomicUserbot**! [🪐](t.me/AtomicUserbot)")

    
@bot.on(dev_cmd(pattern="own", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"[𝙇𝙚𝙤⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣](t.me/leoatomic) è il 🤴🏻 **Creatore** (fiko [😎](t.me/AtomicUserbot)) di questo Userbot!")
