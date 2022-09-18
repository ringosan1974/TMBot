import asyncio
import disnake
import random


from disnake.ext import commands
from enum import Enum


class NotifyComingVC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None and before.channel is None:
            vc = member.voice.channel
            channel = member.guild.system_channel
            await channel.send(f'{member.name if member.nick is None else member.nick}さんが{vc}へ入室しました。')


class CrazySlot(commands.Cog):
    class Words(Enum):
        TWO = '２か。。。ハズレだ'
        THREE = '良い判断だキルア　そのままゴンを連れて逃げろ　それまでは時間を稼ぐ！！'
        FOUR = 'もういい　消えろ'
        CRAZYSLOT = '口の中にルーレット!! 数字は１から９ 出た目によって武器が変わる!!\nそれがオレ様"気狂いピエロ"さ!!\nいい目が出ろよ!!\n'

    def __init__(self, bot):
        self.bot = bot

    def slot(self):
        result = random.randint(2, 4)
        word = TWO if result == 2 else THREE if result == 3 else FOUR
        return word, result

    @commands.slash_command(options=[disnake.Option(name='all', type=disnake.OptionType.boolean, required=False)])
    async def crazyslot(self, interaction: disnake.ApplicationCommandInteraction, all: bool=False):
        word = ''
        if all is True:
            word += CRAZYSLOT
        word += 'ドゥルルルル...'
        await interaction.response.send_message(word)
        await asyncio.sleep(2)
        kaito_words, value = self.slot()
        word = f'{word}{value}!!\nカイト「{kaito_words}」'
        await interaction.edit_original_message(str(word))


def setup(bot):
    bot.add_cog(NotifyComingVC(bot))
    bot.add_cog(CrazySlot(bot))
