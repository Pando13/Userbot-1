import asyncio
import time
from asyncio import sleep
from os import remove
from datetime import datetime
from telethon import events
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, bot, ALIVE_NAME, TG_ID
from userbot.system import register, errors_handler

# ================= CONSTANT =================
BOTLOG = True
BOTLOG_CHATID = Var.PRIVATE_GROUP_ID
TELEGRAM_ID = str(TG_ID)
# ============================================

@register(outgoing=True, pattern=r"^.salva")
@errors_handler
async def log(log_text):
    """ Col comando .salva, salva un messaggio """
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(TELEGRAM_ID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(TELEGRAM_ID, textx)
        else:
            await log_text.edit(f"**Inserisci il messaggio da salvare**")
            return
        await log_text.edit(f"**Messaggio salvato ✅**")
    else:
        await log_text.edit(f"**Serve il log attivo per funzionare!**")
    await sleep(2)
    await log_text.delete()
