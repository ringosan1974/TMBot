import disnake
import re
import msg_img

from disnake.ext import commands

class AddEmoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_attachment(self, url: str):
        ids = msg_img.get_element_from_url(url)
        channel = await self.bot.fetch_channel(ids[0])
        message = await channel.fetch_message(ids[1])
        attach = await message.attachments[0].read()
        return attach

    @commands.slash_command(default_member_permissions=disnake.Permissions(administrator=True))
    async def add_emoji(self, inter: disnake.ApplicationCommandInteraction, name: str, url: str):
        guild = inter.guild
        image = await self.get_attachment(url)
        try:
            await guild.create_custom_emoji(name=name, image=image)
            await inter.response.send_message(f"画像を{name}としてemojiに追加します。")
        except disnake.HTTPException:
            await inter.response.send_message("<HTTPError.> 名前に':'を含まない、2MB以下の画像にしてください。それでも解決しない場合は開発者へご連絡ください。")
