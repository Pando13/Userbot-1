# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
"""AFK Plugin
Syntax: .afk REASON"""

import asyncio
import datetime
from datetime import datetime
from userbot import bot
from telethon import events
from telethon.tl import functions, types

# =================== CONSTANT ===================
global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}
# ============================================


@bot.on(events.NewMessage(pattern=r"\.afk ?(.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await bot(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(
                types.InputPrivacyKeyStatusTimestamp()
            )
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await bot.send_message(event.chat_id, f"**Fuck, Ora vado AFK ⛔️** __MOTIVO ~ {reason}__")
        else:
            await bot.send_message(event.chat_id, f"**Fuck, Ora sono AFK!**")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await bot.send_message(  # pylint:disable=E0602
                Var.PRIVATE_GROUP_ID,  # pylint:disable=E0602
                f"AFK ON {reason}"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@bot.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        shite = await bot.send_message(event.chat_id, "__Fuck, non sono più AFK!__\n**Ora puoi scrivermi.**\nSono stato afk per:`" + total_afk_time + "`")
        try:
            await bot.send_message(  # pylint:disable=E0602
                Var.PRIVATE_GROUP_ID,  # pylint:disable=E0602
                "AFK OFF "
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await bot.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Inserisci la Var `PRIVATE_GROUP_ID` " + \
                "per far funzionare afk " + \
                "in @IOIIOIIIOIIOI\nCerca #pmpermessi per info.\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@bot.on(events.NewMessage(  # pylint:disable=E0602
    incoming=True,
    func=lambda e: bool(e.mentioned or e.is_private)
))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    afk_since = "**a while ago**"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if afk_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                afk_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = f"**⛔️ IL MIO CAPO È OFF ⛔️ DA** `{total_afk_time}`\n**QUINDI NON SPAMMARE GRAZIE.**" + \
            f"\n\n**QUANDO SONO ONLINE RISPONDO A TUTTI BYE.**\n**MOTIVO**: {reason}" \
            if reason \
            else f"**⛔️ AL MOMENTO SONO OFF ⛔️**\n\n**LASCIA UN MESSAGGIO SE DEVI CHIEDERMI QUALCOSA GRAZIE ‼️**\n**APPENA TORNO CERCO DI RISPONDERE BYE 👍**"
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602
