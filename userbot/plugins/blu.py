from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("blu (.*)"))
async def _(event):
	input_str = event.pattern_match.group(1)
	caption = """<a href='tg://user?id='>{}</a>""".format(input_str)
	await event.edit(caption, parse_mode="HTML")
