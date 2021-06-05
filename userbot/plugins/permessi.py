"""Permessi di default
Comandi disponibili: .lock <option>, .unlock <option>, .locks
API Options: msg, media, sticker, gif, game, binline, poll, adduser, pin, changeinfo
DB Options: bots, commands, email, forward, url"""

from telethon import events, functions, types
from userbot.plugins.sql_helper.locks_sql import update_lock, is_locked, get_locks
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"listapermessi", outgoing=True))
async def _(event):
    await event.edit("**Comandi disponibili:** .lock <option>, .unlock <option>, .locks \n**Default:** msg, media, sticker, gif, game, binline, poll, adduser, pin, changeinfo \n**Virtuali:** bots, commands, email, forward, url")


@bot.on(dev_cmd("lock( (?P<target>\S+)|$)"))
async def _(event):
     # Space weirdness in regex required because argument is optional and other
     # commands start with ".lock"
    if event.fwd_from:
        return
    input_str = event.pattern_match.group("target")
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    game = None
    binline = None
    poll = None
    adduser = None
    pin = None
    changeinfo = None
    if input_str:
        if "msg" in input_str:
            msg = True
        if "media" in input_str:
            media = True
        if "sticker" in input_str:
            sticker = True
        if "gif" in input_str:
            gif = True
        if "gamee" in input_str:
            gamee = True
        if "binline" in input_str:
            ainline = True
        if "poll" in input_str:
            gpoll = True
        if "adduser" in input_str:
            adduser = True
        if "pin" in input_str:
            cpin = True
        if "changeinfo" in input_str:
            changeinfo = True
        banned_rights = types.ChatBannedRights(
            until_date=None,
            # view_messages=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=game,
            send_inline=binline,
            send_polls=poll,
            invite_users=adduser,
            pin_messages=pin,
            change_info=changeinfo,
        )
        try:
            result = await bot(  # pylint:disable=E0602
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=peer_id,
                    banned_rights=banned_rights
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(
                "Permessi della chat cambiati correttamente"
            )


@bot.on(dev_cmd("sblocca ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    if input_str in (("bots", "commands", "email", "forward", "url")):
        update_lock(peer_id, input_str, False)
        await event.edit(
            "Sbloccato {}".format(input_str)
        )
    else:
        await event.edit(
            "Usa .lock senza alcun parametro per sbloccarli tutti"
        )


@bot.on(dev_cmd("permessi"))
async def _(event):
    if event.fwd_from:
        return
    res = ""
    current_chat = await event.get_chat()
    try:
        current_api_locks = current_chat.default_banned_rights
    except AttributeError as e:
        logger.info(str(e))
    else:
        res += "🔐 **Blocchi in chat:** \n\n"
        res += "📩 **Messaggi:** `{}`\n".format(current_api_locks.send_messages)
        res += "🖼 **Media:** `{}`\n".format(current_api_locks.send_media)
        res += "🔖 **Sticker:** `{}`\n".format(current_api_locks.send_stickers)
        res += "📹 **Gif:** `{}`\n".format(current_api_locks.send_gifs)
        res += "🎮 **Giochi:** `{}`\n".format(current_api_locks.send_games)
        res += "📟 **Bot Inline:** `{}`\n".format(current_api_locks.send_inline)
        res += "🧮 **Sondaggi:** `{}`\n".format(current_api_locks.send_polls)
        res += "👥 **Aggiungere utenti:** `{}`\n".format(current_api_locks.invite_users)
        res += "🖇 **Fissare messaggi:** `{}`\n".format(current_api_locks.pin_messages)
        res += "🔏 **Cambiare informazioni:** `{}`\n".format(current_api_locks.change_info)
    await event.edit(res)
