import asyncio
import io

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot.system import dev_cmd, command



@command(pattern="^.block ?(.*)")
async def block_pm(event):
    "To block a user."
    if event.is_private:
        user = await event.get_chat()
    else:
        user, reason = await get_full_user(event)
        if not user:
            return
    if not reason:
        reason = "Not Mentioned."
    await event.client(functions.contacts.BlockRequest(user.id))
    await event.edit("**Sei stato bloccato, non puoi inviarmi messaggi**[{}](tg://user?id={})".format(firstname, user.id))
                
                
                
                
@command(pattern="^.unblock ?(.*)")
async def unblock_p_m(event):
    "To unblock a user."
    if event.is_private:
        user = await event.get_chat()
    else:
        user, reason = await get_full_user(event)
        if not user:
            return
    if not reason:
        reason = "Not Mentioned."
    await event.client(functions.contacts.UnBlockRequest(user.id))
    await event.edit("**Sei stato sbloccato, puoi inviarmi messaggi**[{}](tg://user?id={})".format(firstname, user.id))
                
async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
