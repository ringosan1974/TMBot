import disnake
import re


from disnake.ext import commands
from ..util import get_ids_from


class AddEmoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(default_member_permissions=disnake.Permissions(administrator=True))
    async def add_emoji(self, inter: disnake.ApplicationCommandInteraction, name: str, url: str):
        image = await self.get_attachment(url)
        try:
            await inter.guild.create_custom_emoji(name=name, image=image)
            await inter.response.send_message(f"画像を{name}としてemojiに追加します。")
        except disnake.HTTPException:
            await inter.response.send_message("HTTPError.")

    async def get_attachment(self, url: str):
        ids = get_ids_from(url)
        channel = await self.bot.fetch_channel(ids[0])
        message = await channel.fetch_message(ids[1])
        attach = await message.attachments[0].read()
        return attach
