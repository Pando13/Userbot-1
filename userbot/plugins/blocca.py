import asyncio
import io

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, LESS_SPAMMY, bot
from userbot.system import dev_cmd, command


@command(pattern="^.block ?(.*)")
async def blockpm(block):
    if block.pattern_match.group(1):
        username = block.pattern_match.group(1)
        bname = await block.client.get_entity(username)
        name0 = str(bname.first_name)
        uid = await block.client.get_peer_id(username)
    
    elif block.is_private:
        bname= await block.client.get_entity(block.chat_id)
        name0 = str(bname.first_name)
        uid = block.chat_id
                
    elif block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client(GetFullUserRequest(reply.from_id))
        name0 = str(replied_user.user.first_name)
        uid = replied_user.user.id
        
    else:
        x = await block.edit("Gimme the user to block!")
        return await delete_in(x, 5)
    
    if await is_blocked(uid) is True:
        x = await block.edit("The user is already in your block list.")
        return await delete_in(x, 5)
        
    if block.pattern_match.group(1):
        block.reply(f"[{name0}](tg://user?id={uid}) is gonna get blocked in 2 seconds.")
        asyncio.sleep(4)
    elif block.is_private:
        block.reply("I am blocking you now.")
        asyncio.sleep(4)
    elif block.reply_to_msg_id:
        block.edit("You are going to be blocked from PM-ing me now.")
        asyncio.sleep(4)
    
    await block.client(BlockRequest(uid))
    await block_pm(uid)
    await block.edit("***BLOCKED!!***")
    

@command(pattern="^.block ?(.*)")
async def unblockpm(unblock):
    if unblock.pattern_match.group(1):
        username = unblock.pattern_match.group(1)
        ubname = await unblock.client.get_entity(username)
        name0 = str(ubname.first_name)
        uid = await unblock.client.get_peer_id(username)
    
    elif unblock.is_private:
        x = unblock.edit("You aren't serious, right?")
        return await delete_in(x, 5)
                   
    elif unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client(GetFullUserRequest(reply.from_id))
        name0 = str(replied_user.user.first_name)
        uid = replied_user.user.id
       
    
    else:
        x = await unblock.edit("I can't unblock '__NOBODY__'")
        return await delete_in(x, 5)
    
    if await is_blocked(uid) is False:
        x = await unblock.edit("The user isn't blocked...yet.")
        return await delete_in(x, 5)
    
    if unblock.pattern_match.group(1):
        unblock.edit(f"I will unblock [{name0}](tg://user?id={uid}) in 2 seconds. Are you sure?")
        asyncio.sleep(4)
    elif unblock.reply_to_msg_id:
        unblock.edit("You are gonna be unblocked now. Aren't you happy?")
        asyncio.sleep(4)
        
    await unblock.client(UnblockRequest(uid))
    await unblock_pm(uid)
    await unblock.edit("Let's make peace.")

    
    
    
