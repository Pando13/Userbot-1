from telethon import functions

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.dc")
async def neardc(event):
    """ con .dc, ottieni info sl datacenter. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Paese : `{result.country}` \n"
                     f"DC più vicino: `{result.nearest_dc}` \n"
                     f"Questo DC : `{result.this_dc}`")
