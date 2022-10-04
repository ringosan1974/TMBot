import disnake


from disnake.ext import commands


from notify_vc import NotifyComingVC
from crazyslot import CrazySlot


def setup(bot):
    bot.add_cog(NotifyComingVC(bot))
    bot.add_cog(CrazySlot(bot))
