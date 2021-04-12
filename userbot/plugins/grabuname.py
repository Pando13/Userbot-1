from telethon import events, TelegramClient, sync
from telethon.tl.functions.account import UpdateUsernameRequest
import threading, requests, time, random
import asyncio
from userbot import bot
from userbot.system import dev_cmd


state = False
time1 = time.time()
new_username = ''

@bot.on(dev_cmd(pattern="grabun", outgoing=True))
def check_username():
    global new_username, state, time1

    while True:
        r = requests.get('https://t.me/' + new_username)

        if 'https://telegram.org/img/t_logo.png' in r.text:
            time1 = time.time()
            state = True
            break
        elif r.status_code == 200 and 'twitter:image' in r.text:
            print("checking username {0}".format('.'*random.randrange(1, 5)+' '*5), end="\r")
        else:
            print('no response from telegram')


new_username = input('enter target username: ')

client = TelegramClient('session_file', api_id, api_hash).start()

t = threading.Thread(target=check_username)
t.setDaemon(True)
t.start()

while True:
    if state == True:
        client(UpdateUsernameRequest(new_username))
        print('username chenged in {0:.2f} seconds after last check.'.format(time.time() - time1))
        break

input('press enter to exit')
