"""Get Telegram Profile and other information
Syntax:
.dc
.chatinfo
.info @username
.stats
"""

import asyncio
import time
import sys
import html

from datetime import datetime
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import User, Chat, Channel
from telethon.tl.types import MessageActionChannelMigrateFrom, MessageEntityMentionName, ChannelParticipantsAdmins 
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon import events, functions
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from userbot import CMD_HELP, bot, ALIVE_NAME
from userbot.system import dev_cmd, register, errors_handler

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================




@bot.on(dev_cmd("dc"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "Need a Profile Picture to check **this**"
        location = str(e)
    await event.send_message(f"**🌍 DC**: {dc_id}")

    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = event.message.id
    await bot.send_message(
        event.chat_id,
        caption,
        reply_to=message_id_to_reply,
 
        file=replied_user.profile_photo,
        force_document=False,
        silent=True
    )
    await event.delete()


