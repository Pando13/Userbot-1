"""
Available Commands:
.autoblu"""

from telethon import events

import asyncio





@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "autoblu":

        await event.edit(input_str)

        animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:00 ▱▱▱▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ▶️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:01 ▰▱▱▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:02 ▰▰▱▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:03 ▰▰▰▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:04 ▰▰▰▰▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:05 ▰▰▰▰▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",    
            "⬤⬤◯ 79% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:06 ▰▰▰▰▰▰▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤◯ 79% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:07 ▰▰▰▰▰▰▰▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤◯ 78% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:08 ▰▰▰▰▰▰▰▰▱▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤◯ 78% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:09 ▰▰▰▰▰▰▰▰▰▱ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏸️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71",
            "⬤⬤◯ 77% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✖️\n\n⠀⠀⠀⠀⠀@Leoatomic's Music Player\n\n⠀⠀⠀⠀In riproduzione: Shiva Auto Blu feat. Eiffel 65\n\n00:10 ▰▰▰▰▰▰▰▰▰▰ 00:10\n\n⠀⠀⠀⠀⠀🔂 ⏮️ ⏪️ ⏺️ ⏩️ ⏭️\n\n⠀Next Song: Mh ah ah - Young Signorino.\n\n⠀⠀⠀⠀⠀Device: Galaxy A71"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
