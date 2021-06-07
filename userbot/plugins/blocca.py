import asyncio
import io

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, LESS_SPAMMY, bot
from userbot.system import dev_cmd, command


@command(pattern="^.block ?(.*)")
async def block_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.disapprove(chat.id)
            await event.edit("**Sei stato bloccato, non puoi inviarmi messaggi**[{}](tg://user?id={})".format(firstname, chat.id))
            await event.client(functions.contacts.BlockRequest(chat.id))
                
            
@command(pattern="^.unblock ?(.*)")
async def unblock_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if pmpermit_sql.disapprove(chat.id)
            pmpermit_sql.is_approved(chat.id):
            await event.edit("**Sei stato sbloccato, puoi inviarmi messaggi**[{}](tg://user?id={})".format(firstname, chat.id))
            await event.client(functions.contacts.UnBlockRequest(chat.id))
        
