"""Snips
Available Commands:
.comando
.lcomandi
.dcomando"""


import io
from telethon import events, utils
from telethon.tl import types
from userbot.plugins.sql_helper.snips_sql import get_snips, add_snip, remove_snip, get_all_snips
from userbot import bot
from userbot.system import dev_cmd


TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2


@bot.on(events.NewMessage(pattern=r'\.(\S+)', outgoing=True))
async def on_snip(event):
    name = event.pattern_match.group(1)
    snip = get_snips(name)
    if snip:
        if snip.snip_type == TYPE_PHOTO:
            media = types.InputPhoto(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference
            )
        elif snip.snip_type == TYPE_DOCUMENT:
            media = types.InputDocument(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference
            )
        else:
            media = None
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        await bot.send_message(
            event.chat_id,
            snip.reply,
            reply_to=message_id,
            file=media
        )
        await event.delete()


@bot.on(dev_cmd("comando (.*)"))
async def on_snip_save(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {'type': TYPE_TEXT, 'text': msg.message or ''}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip['type'] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip['type'] = TYPE_DOCUMENT
            if media:
                snip['id'] = media.id
                snip['hash'] = media.access_hash
                snip['fr'] = media.file_reference
        add_snip(name, snip['text'], snip['type'], snip.get('id'), snip.get('hash'), snip.get('fr'))
        await event.edit("**Comando __{name}__ salvato ✅ \nOttienilo con:** `.{name}`".format(name=name))
    else:
        await event.edit("Non ci sono comandi. Salvane con `.comando`")


@bot.on(dev_cmd("lcomandi"))
async def on_snip_list(event):
    all_snips = get_all_snips()
    OUT_STR = "**Comandi disponibili:**\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"- #{a_snip.snip} \n"
    else:
        OUT_STR = "Non ci sono comandi. Salvane con `.comando`"
    if len(OUT_STR) > 4095:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "comandi.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Comandi disponibili:",
                reply_to=event
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)


@bot.on(dev_cmd("dcomando (\S+)"))
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_snip(name)
    await event.edit("**Comando #{} eliminato ✅**".format(name))
