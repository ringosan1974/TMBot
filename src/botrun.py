import asyncio
import disnake
import notify_time


from var import TOKEN


def run(bot):
    try:
        loop = asyncio.get_event_loop()
        for t, msg in zip(notify_time.nt_time, notify_time.nt_msg):
            loop.create_task(notify_time.run_at(t, notify_time.NotifyTime(t.hour, msg, bot)))
        loop.create_task(bot.start(TOKEN))
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.stop()
