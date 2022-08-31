import disnake
import os
import cogs

from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='tm!', intents=disnake.Intents.all(), sync_commands_debug=True)
bot.load_extension('cogs')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(TOKEN)
