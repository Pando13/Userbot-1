from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd("menziona (.*)"))
async def _(event):
	if event.fwd_from:
		return	
	input_str = event.pattern_match.group(1)
	if event.reply_to_msg_id:
		r_msg = await event.get_reply_message()
		if r_msg.forward:
			replied_user = r_msg.forward.from_id
		else:
			replied_user = r_msg.from_id
	else:
		await event.edit("Rispondi ad un messaggio")
	user_id = replied_user
	caption = """<a href='tg://user?id={}'>{}</a>""".format(str(r_msg.from_id.user_id), input_str)	
	await event.edit(caption, parse_mode="HTML")
