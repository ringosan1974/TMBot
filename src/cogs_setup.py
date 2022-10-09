import disnake


from disnake.ext import commands


from crazyslot import CrazySlot
from msg_img import CreateMessageImage
from notify_vc import NotifyComingVC


def setup(bot):
    bot.add_cog(CrazySlot(bot))
    bot.add_cog(CreateMessageImage(bot))
    bot.add_cog(NotifyComingVC(bot))
