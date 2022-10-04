import asyncio
import datetime
import disnake


from disnake.ext import commands


nt_time = [
    datetime.time(0),
    datetime.time(12)
]

nt_msg = [
    '零時です。',
    'お昼です。'
]


async def wait_for(time: datetime.time):
    now = datetime.datetime.now().time()
    remaining = datetime.timedelta(
                    hours = time.hour - now.hour,
                    minutes = time.minute - now.minute,
                    seconds = time.second - now.second
                ).total_seconds()
    if remaining < 0:
        remaining += datetime.timedelta(days=1).total_seconds()
    await asyncio.sleep(remaining)


async def run_at(time: datetime.time, func):
    await wait_for(time)
    return await func


async def NotifyTime(hour: int, msg: str, bot: commands.Bot):
    for guild in bot.guilds:
        if guild.system_channel != None:
            await guild.system_channel.send(msg)
