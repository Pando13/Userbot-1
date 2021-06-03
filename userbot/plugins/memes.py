""" Userbot module for having some fun with people. """

import asyncio
import random
import re
import time
import requests

from collections import deque

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from telethon import events

from cowpy import cow

from userbot import CMD_HELP,YOUTUBE_API_KEY, bot
from userbot.system import register, dev_cmd

# ================= CONSTANT =================


DADO = [
    "**È uscito:** 1 🎲",
    "**È uscito:** 2 🎲",
    "**È uscito:** 3 🎲",
    "**È uscito:** 4 🎲",
    "**È uscito:** 5 🎲",
    "**È uscito:** 6 🎲",
]

INSULT_STRINGS = [
     "Comando non trovato. Proprio come il tuo cervello.",
    "La regola 420 del bot, sezione 69, mi impedisce di rispondere ai coglioni come te.",
    "Scommetto che il tuo cervello si sente come nuovo, visto che non lo usi mai.",
    "Se volessi uccidermi, scalerei il tuo ego e salterei sul tuo QI.",
    "Non ti sei evoluto dalle scimmie, si sono evolute loro da te.",
    "In che lingua stai parlando? Perché suona come una stronzata.",
    "Sei la prova che l'evoluzione può andare al contrario.",
    "Di solito le persone vivono e imparano. Tu vivi e basta.",
    "Continua a parlare, un giorno dirai qualcosa di intelligente!... (ne dubito).",
    "Tutti hanno il diritto di essere stupidi ma tu stai abusando del privilegio.",
    "Mi dispiace di aver ferito i tuoi sentimenti quando ti ho chiamato stupido. Pensavo lo sapessi già.",
    "Dovresti provare ad assaggiare il cianuro.",
    "Dovresti provare a dormire per sempre.",
    "Prendi una pistola e sparati.",
    "Prova a fare il bagno con acido cloridrico anziché con acqua.",
    "Dovresti offrirti come volontario per un bersaglio al poligono di tiro.",
    "Le persone come te sono la ragione per cui abbiamo il dito medio.",
    "Sei così brutto che quando piangi, le lacrime scendono lungo la tua testa... solo per evitare il tuo viso.",
    "Se parli alle mie spalle, sei in una posizione perfetta per baciarmi il culo!",
]



SHGS = [
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "ლ(ﾟдﾟლ)",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "ლ｜＾Д＾ლ｜",
    "ლ（╹ε╹ლ）",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    "¯\_(ツ)_/¯",
    "¯\_(⊙_ʖ⊙)_/¯",
]


# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")

@register(outgoing=True, pattern="^:c$")
async def kek(keks):
    if not keks.text[0].isalpha() and keks.text[0] not in ("/", "#", "@", "!"):
        """ Check yourself ;)"""
        uio = ["c", "ɔɔ"]
        for i in range(1, 15):
            time.sleep(0.3)
            await keks.edit(":" + uio[i % 2])

@register(outgoing=True, pattern=r"^.coinflip (.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        if event.fwd_from:
            return
        r = random.randint(1, 100)
        input_str = event.pattern_match.group(1)
        if input_str:
            input_str = input_str.lower()
        if r % 2 == 1:
            if input_str == "testa":
                await event.edit("**Testa**.\nHai indovinato.")
            elif input_str == "tails":
                await event.edit("**Testa**.\nNon hai indovinato")
            else:
                await event.edit("**Testa**")
        elif r % 2 == 0:
            if input_str == "croce":
                await event.edit("**Croce**.\nHai indovinato.")
            elif input_str == "heads":
                await event.edit("**Croce**.\nNon hai indovinato")
            else:
                await event.edit("**Croce**")
        else:
            await event.edit("Cambia moneta, questa è falsa..")

@bot.on(dev_cmd(pattern="own", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"[𝙇𝙚𝙤⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣](t.me/leoatomic) è il 🤴🏻 **Creatore** (fiko [😎](t.me/AtomicUserbot)) di questo Userbot!")			  
		


@register(outgoing=True, pattern="^.dado$")
async def dado(e):
    """Tira un dado!"""
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(DADO))
			  
@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(INSULT_STRINGS))


@register(outgoing=True, pattern="^.bt$")
async def bluetext(bte):
    """ Believe me, you will find this useful. """
    if not bte.text[0].isalpha() and bte.text[0] not in ("/", "#", "@", "!"):
        if await bte.get_reply_message():
            await bte.edit(
                "⁣/TESTO /BLU /DEVO /CLICCARE\n"
                "/SONO /UNO /STUPIDO /ANIMALE /ATTRATTO /DAI /COLORI"
            )


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await shg.edit(random.choice(SHGS))



@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha() and memereview.text[0] not in ("/", "#", "@", "!"):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)

@register(outgoing=True, pattern="^.smk (.*)")
async def smrk(smk):
        if not smk.text[0].isalpha() and smk.text[0] not in ("/", "#", "@", "!"):
            textx = await smk.get_reply_message()
            message = smk.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)
        if message == 'dele':
            await smk.edit( message +'te the hell' + "ツ" )
            await smk.edit("ツ")
        else:
             smirk = " ツ"
             reply_text = message + smirk
             await smk.edit(reply_text)


@register(outgoing=True, pattern=r".yt_dl (\S*) ?(\S*)")
async def download_video(v_url):
    """ For .yt_dl command, download videos from YouTube. """
    if not v_url.text[0].isalpha() and v_url.text[0] not in ("/", "#", "@", "!"):
        url = v_url.pattern_match.group(1)
        quality = v_url.pattern_match.group(2)

        await v_url.edit("**Raccolgo...**")

        video = YouTube(url)

        if quality:
            video_stream = video.streams.filter(
                progressive=True,
                subtype="mp4",
                res=quality
            ).first()
        else:
            video_stream = video.streams.filter(
                progressive=True,
                subtype="mp4"
            ).first()

        if video_stream is None:
            all_streams = video.streams.filter(
                progressive=True,
                subtype="mp4"
            ).all()
            available_qualities = ""

            for item in all_streams[:-1]:
                available_qualities += f"{item.resolution}, "
            available_qualities += all_streams[-1].resolution

            await v_url.edit(
                "**A stream matching your query wasn't found. Try again with different options.\n**"
                "**Available Qualities:**\n"
                f"{available_qualities}"
            )
            return

        video_size = video_stream.filesize / 1000000

        if video_size >= 50:
            await v_url.edit(
                ("**File larger than 50MB. Sending the link instead.\n**"
                 f"Get the video [here]({video_stream.url})\n\n"
                 "**If the video plays instead of downloading, right click(or long press on touchscreen) and "
                 "press 'Save Video As...'(may depend on the browser) to download the video.**")
            )
            return

        await v_url.edit("**Scarico...**")

        video_stream.download(filename=video.title)

        url = f"https://img.youtube.com/vi/{video.video_id}/maxresdefault.jpg"
        resp = get(url)
        with open('thumbnail.jpg', 'wb') as file:
            file.write(resp.content)

        await v_url.edit("**Carico...**")
        await v_url.client.send_file(
            v_url.chat_id,
            f'{safe_filename(video.title)}.mp4',
            caption=f"{video.title}",
            thumb="thumbnail.jpg"
        )

        os.remove(f"{safe_filename(video.title)}.mp4")
        os.remove('thumbnail.jpg')
        await v_url.delete()
