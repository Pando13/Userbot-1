# Userbot-Leoatomic


[![Made in Python](https://img.shields.io/badge/Made%20in-python-red.svg)](https://www.python.org/)

## INSTALLAZIONE

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fleoatomic%2Fuserbot&template=https%3A%2F%2Fgithub.com%2Fleoatomic%2Fuserbot)

### Var Obbligatorie

- Solo queste due variabili sono obbligatorie:
  - `APP_ID`: Valore da ottenere da <https://my.telegram.org>
  - `API_HASH`: Valore da ottenere da <https://my.telegram.org>
- Se non ci sono causerà: `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

***
```bash
> API ID e API HASH
```
Vai sul [sito di telegram](my.telegram.org/), esegui il login e clicca su `API DEVELOPMENT TOOLS`. Dopodiché compila i campi richiesti e salva le due stringhe `API_ID` e `API_HASH`.

***

```bash
> String Session
```
Vai su [questo sito](repl.it/@Ilas69/generatestringsession) e clicca su `RUN` in alto. Dopo aver atteso e compilato i campi richiesti dalla console (attenzione, il numero deve essere inserito con il prefisso, es: +393117290283) ti arriverà la stringa nei messaggi salvati di Telegram.

***

```bash
> Chat ID
```
Vai su Telegram, crea un gruppo e aggiungi `@GroupHelpBot` come amministratore con tutti i permessi. Fatto ciò esegui il comando `.chatid` nel gruppo e salva la stringa che esce.

***

```bash
> Token
```
Vai su `@BotFather`, crea un bot con `/newbot`, dai un nome e nickname a piacere e salva il Token del bot. Dopodiché esegui il comando `/setinline` sempre su BotFather, seleziona l'ultimo bot creato, digita una qualsiasi cosa in chat e inviala.

***

```bash
> Heroku
```
Ora devi andare su heroku.com e creare un account. Successivamente vai qui https://heroku.com/deploy e compila i campi richiesti del modo seguente:
```yaml
ALIVE_NAME: Il tuo nickname di Telegram (con o senza @).
API_HASH: L'omonima stringa ricavata nel primo step.
APP_ID: L'omonima stringa ricavata nel primo step.
PRIVATE_GROUP_ID: Il chat-id ricevuto da GroupHelpBot.
STRING_SESSION: La stringa lunga ricevuta nei messaggi salvati.
TG_BOT_TOKEN_BF_HER: Il token del bot generato da BotFather.
TG_BOT_USER_NAME_BF_HER: Il link del vostro bot presente nel messaggio di BotFather (es: t.me/NomeDelBot).
```
Dopo aver compilato i campi precedenti devi cliccare `Deploy app` in basso e aspettare che si carichi. Successivamente devi, nella pagina dell'applicazione, andare sulla seconda icona viola, cliccare sulla matita vicino al pulsante e abilitarlo. Dopodiché clicca il tasto `More` e, nel menu a tendina che ti apparirà clicca `Logs`.

***

#### CONTATTI:

[![Telegram](https://img.shields.io/badge/TG-%20@Leoatomic-black.svg)](https://t.me/Leoatomic)
