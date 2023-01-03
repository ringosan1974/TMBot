import disnake


from disnake.ext import commands
from ..util import get_user_name


class NotifyVCState(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await self._notify_afk(member, before, after)
        await self._notify_connected(member, before, after)

    async def _notify_afk(self, member, before, after):
        name = NotifyVCState._get_user_name(member)
        if after.self_deaf is True and before.self_deaf is False:
            await member.guild.system_channel.send(f'{name}さんが離席中です。')
        if after.self_deaf is False and before.self_deaf is True:
            await member.guild.system_channel.send(f'{name}さんが離席解除しました。')

    async def _notify_connected(self, member, before, after):
        try:
            name = NotifyVCState._get_user_name(member)
            if after.channel is not None and before.channel is None:
                vc = after.channel.name
                await member.guild.system_channel.send(f'{name}さんが{vc}へ入室しました。')
            if after.channel is None and before.channel is not None:
                vc = before.channel.name
                await member.guild.system_channel.send(f'{name}さんが{vc}から退出しました。')
        except disnake.HTTPException as e:
            await member.guild.system_channl.send(f"HTTPError: {e}")
