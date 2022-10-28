import asyncio
import disnake
import random


from disnake.ext import commands
from enum import Enum


class Words(Enum):
    TWO = '２か。。。ハズレだ'
    THREE = '良い判断だキルア　そのままゴンを連れて逃げろ　それまでは時間を稼ぐ！！'
    FOUR = 'もういい　消えろ'
    CRAZYSLOT = '口の中にルーレット!! 数字は１から９ 出た目によって武器が変わる!!\nそれがオレ様"気狂いピエロ"さ!!\nいい目が出ろよ!!\n'


class CrazySlot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __slot(self):
        result = random.randint(2, 4)
        word = Words.TWO.value if result == 2 else Words.THREE.value if result == 3 else Words.FOUR.value
        return word, result

    @commands.slash_command(options=[disnake.Option(name='all', type=disnake.OptionType.boolean, required=False)])
    async def crazyslot(self, interaction: disnake.ApplicationCommandInteraction, all: bool=False):
        word = ''
        if all is True:
            word += CRAZYSLOT
        word += 'ドゥルルルル...'
        await interaction.response.send_message(word)
        await asyncio.sleep(2)
        kaito_words, value = self.__slot()
        word = f'{word}{value}!!\nカイト「{kaito_words}」'
        await interaction.edit_original_message(str(word))
