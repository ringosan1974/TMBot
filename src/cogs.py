import asyncio
import disnake
import random

from disnake.ext import commands

class NoticeComingVC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.voice is not None:
            vc = member.voice.channel
            channel = member.guild.system_channel
            await channel.send(f'{member.name if member.nick is None else member.nick}さんが{vc}へ入室しました。')

kaito_words = ['２か...ハズレだ', '良い判断だキルア そのままゴンを連れて逃げろ それまでは時間を稼ぐ!!', 'もういい 消えろ']

class CrazySlot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def slot(self):
        result = random.randint(2, 4)
        return result

    @commands.slash_command()
    async def crazyslot(self, interaction: disnake.ApplicationCommandInteraction, short=False):
        word = ''
        if short is False:
            word += '口の中にルーレット!! 数字は１から９ 出た目によって武器が変わる!!\nそれがオレ様"気狂いピエロ"さ!!\nいい目が出ろよ!!\n'
        word += 'ドゥルルルル...'
        await interaction.response.send_message(word)
        await asyncio.sleep(2)
        value = self.slot()
        word = f'{word}{value}!!\nカイト「{kaito_words[value-2]}」'
        await interaction.edit_original_message(str(word))

def setup(bot):
    bot.add_cog(NoticeComingVC(bot))
    bot.add_cog(CrazySlot(bot))
