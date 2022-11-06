import disnake

from disnake.ext import commands
from add_emoji import AddEmoji
from crazyslot import CrazySlot
from msg_img import CreateMessageImage
from notify_vc import NotifyComingVC
from omikuji import Omikuji

def setup(bot):
    bot.add_cog(CrazySlot(bot))
    bot.add_cog(CreateMessageImage(bot))
    bot.add_cog(NotifyComingVC(bot))
    bot.add_cog(AddEmoji(bot))
    bot.add_cog(Omikuji(bot))