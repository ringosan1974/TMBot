import disnake


from disnake.ext import commands
from commands.add_emoji import AddEmoji
from commands.crazyslot import CrazySlot
from commands.msg_img import CreateMessageImage
from commands.notify_vc import NotifyVCState
from commands.omikuji import Omikuji


def setup(bot):
    bot.add_cog(CrazySlot(bot))
    bot.add_cog(CreateMessageImage(bot))
    bot.add_cog(NotifyVCState(bot))
    bot.add_cog(AddEmoji(bot))
    bot.add_cog(Omikuji(bot))