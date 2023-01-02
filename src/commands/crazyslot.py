import asyncio
import disnake
import random


from disnake.ext import commands
from enum import Enum
from ..var import Words


class CrazySlot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(options=[disnake.Option(name='all', type=disnake.OptionType.boolean, required=False)])
    async def crazyslot(self, interaction: disnake.ApplicationCommandInteraction, all: bool=False):
        word = ''
        if all is True:
            word += Words.CRAZYSLOT
        word += 'ドゥルルルル...'
        await interaction.response.send_message(word)
        await asyncio.sleep(2)
        kaito_words, value = CrazySlot._slot()
        word = f'{word}{value}!!\nカイト「{kaito_words}」'
        await interaction.edit_original_message(str(word))

    @staticmethod
    def _slot():
        result = random.randint(2, 4)
        word = Words.TWO.value if result == 2 else Words.THREE.value if result == 3 else Words.FOUR.value
        return word, result
