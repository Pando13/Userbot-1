import os
import re

from telethon import Button
from userbot.system import dev_cmd
from userbot.plugins import TG_BOT_USER_NAME_BF_HER

# regex obtained from:
# https://github.com/PaulSonOfLars/tgbot/blob/master/tg_bot/modules/helper_funcs/string_handling.py#L23
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@bot.on(dev_cmd(pattern=r"cbutton ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "`Che testo devo usare`")
    prev = 0
    note_data = ""
    buttons = []
    for match in BTN_URL_REGEX.finditer(markdown_note):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1
        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            # create a thruple with button label, url, and newline status
            buttons.append((match.group(2), match.group(3), bool(match.group(4))))
            note_data += markdown_note[prev : match.start(1)]
            prev = match.end(1)
        # if odd, escaped -> move along
        elif n_escapes % 2 == 1:
            note_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1
        else:
            break
    else:
        note_data += markdown_note[prev:]
    message_text = note_data.strip() or None
    tl_ib_buttons = build_keyboard(buttons)
    tgbot_reply_message = None
    if reply_message and reply_message.media:
        tgbot_reply_message = await event.client.download_media(reply_message.media)
    if tl_ib_buttons == []:
        tl_ib_buttons = None
    await tgbot.send_message(
        entity=event.chat_id,
        message=message_text,
        parse_mode="html",
        file=tgbot_reply_message,
        link_preview=False,
        buttons=tl_ib_buttons,
    )
    await event.delete()
    if tgbot_reply_message:
        os.remove(tgbot_reply_message)


# Helpers


@bot.on(dev_cmd(pattern=r"ibutton ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    # soon will try to add media support
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "`what text should i use in button post`")
    catinput = "Inline buttons " + markdown_note
    results = await event.client.inline_query(TG_BOT_USER_NAME_BF_HER, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
