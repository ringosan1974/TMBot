import cogs
import disnake

from botrun import run
from disnake.ext import commands

bot = commands.Bot(command_prefix='tm!', intents=disnake.Intents.all(), sync_commands_debug=True)
bot.load_extension('cogs')

@bot.event
async def on_ready():
    print(f'[*] We have logged in as {bot.user}')

run(bot)
