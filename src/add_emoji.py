import disnake
import re
import msg_img

from disnake.ext import commands

def is_correct_name(self, name: str):
    match = re.search(":.*:", name)
    return False if match else True

# return if image size is smaller than 2MB.
def is_smaller_size(image: bytes):
    return image.bit_length() < 21

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
        if is_smaller_size(image) and is_correct_name(name):
            await inter.response.send_message(f"画像を{name}としてemojiに追加します。")
            await guild.create_custom_emoji(name=name, image=image)
        else:
            await inter.response.send_message("Error: 名前に':'を含まない、2MB以内の画像にしてください。")
