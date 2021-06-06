import asyncio
import io

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot.system import dev_cmd, command



@command(pattern="^.block ?(.*)")
async def block_p_m(event):
        if event.fwd_from:
            return
        replied_user, error_i_a = await get_full_user(event)
        if replied_user is None:
            await event.edit(str(error_i_a))
            return False
        user = await event.get_chat()
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        if event.is_private:
          await event.client(functions.contacts.BlockRequest(user.id))
          await event.edit("**Sei stato bloccato, non puoi inviarmi messaggi**[{}](tg://user?id={})".format(firstname, user.id))
                
                
                
                
@command(pattern="^.unblock ?(.*)")
async def unblock_p_m(event):
        if event.fwd_from:
            return
        if event.fwd_from:
            return
        replied_user, error_i_a = await get_full_user(event)
        if replied_user is None:
            await event.edit(str(error_i_a))
            return False
        user = await event.get_chat()
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        if event.is_private:
          await event.client(functions.contacts.UnblockRequest(user.id))
          await event.edit("**Sei stato sbloccato, puoi inviarmi messaggi**[{}](tg://user?id={})".format(firstname, user.id))
                
