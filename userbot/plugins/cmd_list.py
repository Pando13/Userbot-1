
  
from telethon import events
import subprocess
import asyncio
import time
from userbot.system import command

@command(pattern="^.cmd", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"ℹ️ LISTA PLUG-IN 🔍\n\n{o}\n\n"
    await event.edit(OUTPUT)
