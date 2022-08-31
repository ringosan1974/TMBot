import disnake
from disnake.ext import commands

class NoticeComingVC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.voice is not None:
            vc = member.voice.channel
            channel = member.guild.system_channel
            await channel.send(f'{member.name}さんが{vc}へ入室しました。')

def setup(bot):
    bot.add_cog(NoticeComingVC(bot))
