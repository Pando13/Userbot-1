"""Get Telegram Profile and other information
Syntax:
.dc
"""

from telethon import events

@bot.on(dev_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(result.stringify())
