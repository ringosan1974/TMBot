import cogs_setup
import disnake

from disnake.ext import commands
from var import TOKEN

bot = commands.Bot(command_prefix='tm!', intents=disnake.Intents.all(), sync_commands_debug=True)
bot.load_extension('cogs_setup')

@bot.event
async def on_ready():
    print(f'[*] We have logged in as {bot.user}')

bot.run(TOKEN)