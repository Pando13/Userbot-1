"""Get Telegram Profile and other information
Syntax:
.dc

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





@bot.on(dev_cmd("dc"))
async def _(event):
    if event.fwd_from:
        return
    
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "Mi serve una foto profilo per controllare il **DC**"
        location = str(e)
    await event.edit(f"**🌍 DC**: {dc_id}")
    

