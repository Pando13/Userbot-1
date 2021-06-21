import os
from pytgcalls import GroupCall
import ffmpeg
from datetime import datetime
from pyrogram import filters, Client, idle
import requests
import wget
import aiohttp
from random import randint
import aiofiles

VOICE_CHATS = {}
DEFAULT_DOWNLOAD_DIR = '../downloads/vcbot/'

# deezer download web of william butcher bot
ARQ = "https://thearq.tech/"

# userbot and contacts filter by dashezup's tgvc-userbot
self_or_contact_filter = filters.create(
    lambda
    _,
    __,
    message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

# fetch url for deezer download
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

# get args for saavn download
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])



# jiosaavn song download
@bot.on(dev_cmd(filters.command('saavn') & self_or_contact_filter))
async def song(client, message):
    message.chat.id
    message.from_user["id"]
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("Che canzone cerchi? 🧐")
        return ""
    pak = await message.reply('Scaricando...')
    try:
        # @ImJanindu <Infinity BOTs>
        r = requests.get(f"https://jevcplayerbot-saavndl.herokuapp.com/result/?query={args}")
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r.json()[0]["song"]
    slink = r.json()[0]["media_url"]
    ssingers = r.json()[0]["singers"]
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await pak.edit('Carico...')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers)
    os.remove(ffile)
    await pak.delete()

async def _download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name

# deezer download by william butcher bot
@bot.on(dev_cmd(filters.command("deezer") & self_or_contact_filter))
async def deezer(_, message):
    if len(message.command) < 2:
        await message.reply_text("Che canzone cerchi? 🧐")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    hike = await message.reply_text("Cerco...")
    try:
        r = await fetch(f"{ARQ}deezer?query={query}&count=1")
        title = r[0]["title"]
        url = r[0]["url"]
        artist = r[0]["artist"]
    except Exception as e:
        await hike.edit(str(e))
        return
    await hike.edit("Scarico...")
    song = await download_song(url)
    await hike.edit("Carico...")
    await message.reply_audio(audio=song, title=title, performer=artist)
    os.remove(song)
    await hike.delete()

@bot.on(dev_cmd(filters.command('play') & self_or_contact_filter))
async def play_track(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return
    input_filename = os.path.join(
        client.workdir, DEFAULT_DOWNLOAD_DIR,
        'input.raw',
    )
    audio = message.reply_to_message.audio
    audio_original = await message.reply_to_message.download()
    a = await message.reply('Scarico...')
    ffmpeg.input(audio_original).output(
        input_filename,
        format='s16le',
        acodec='pcm_s16le',
        ac=2, ar='48k',
    ).overwrite_output().run()
    os.remove(audio_original)
    if VOICE_CHATS and message.chat.id in VOICE_CHATS:
        text = f'▶️ Riproduco: **{audio.title}**'
    else:
        try:
            group_call = GroupCall(client, input_filename)
            await group_call.start(message.chat.id)
        except RuntimeError:
            await message.reply('Non esiste una chat vocale')
            return
        VOICE_CHATS[message.chat.id] = group_call
    await a.edit(f'▶️ Riproduco: **{audio.title}**')


@bot.on(dev_cmd(filters.command('stopvc') & self_or_contact_filter))
async def stop_playing(_, message):
    group_call = VOICE_CHATS[message.chat.id]
    group_call.stop_playout()
    os.remove('downloads/vcbot/input.raw')
    await message.reply('Chiamata terminata ❌')


@bot.on(dev_cmd(filters.command('joinvc') & self_or_contact_filter))
async def join_voice_chat(client, message):
    input_filename = os.path.join(
        client.workdir, DEFAULT_DOWNLOAD_DIR,
        'input.raw',
    )
    if message.chat.id in VOICE_CHATS:
        await message.reply('Sto già partecipando alla chiamata 🛠')
        return
    chat_id = message.chat.id
    try:
        group_call = GroupCall(client, input_filename)
        await group_call.start(chat_id)
    except RuntimeError:
        await message.reply('errore!')
        return
    VOICE_CHATS[chat_id] = group_call
    await message.reply('Partecipo alla chiamata ✅')


@bot.on(dev_cmd(filters.command('leavevc') & self_or_contact_filter))
async def leave_voice_chat(client, message):
    chat_id = message.chat.id
    group_call = VOICE_CHATS[chat_id]
    await group_call.stop()
    VOICE_CHATS.pop(chat_id, None)
    await message.reply('Esco dalla chiamata ✅')

app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
