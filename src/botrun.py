import asyncio
import disnake
import nt


from var import TOKEN


def run(bot):
    try:
        loop = asyncio.get_event_loop()
        for t, msg in zip(nt.nt_time, nt.nt_msg):
            loop.create_task(nt.run_at(t, nt.NotifyTime(t.hour, msg, bot)))
        loop.create_task(bot.start(TOKEN))
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.stop()
