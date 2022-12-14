import disnake
import io
import os


from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont
from ..var import TRANSPARENT, BLACK, BACKGROUND, FONT, get_ids_from, images_alpha_composite


class CreateMessageImage(commands.Cog):
    def __init__(self, bot, background=BACKGROUND):
        self.bot = bot
        self.background = background

    @commands.slash_command(name='msgimg', description='create image from message')
    async def messageimage(self, inter: disnake.ApplicationCommandInteraction, url: str):
        try:
            ids = get_ids_from(url)
            channel = await self.bot.fetch_channel(ids[0])
            message = await channel.fetch_message(ids[1])

            bytesicon = await message.author.avatar.read()
            icon = Image.open(io.BytesIO(bytesicon))
            image = self._create_msgimg(icon, message.content)
            with io.BytesIO() as bytesimage:
                image.save(bytesimage, format="PNG")
                bytesimage.seek(0)
                await inter.response.send_message(file=disnake.File(bytesimage, filename="file.png"))
        except disnake.HTTPException as e:
            await inter.response.send_message(f"HTTPError: {e}")

    # make and save message-image
    def _create_msgimg(self, avatar: Image, content: str):
        with Image.open(self.background).convert('RGBA') as base:
            font = ImageFont.truetype(FONT, 80)
            text = Image.new("RGBA", base.size, TRANSPARENT)
            icon = Image.new("RGBA", base.size, TRANSPARENT)

            drawtext = ImageDraw.Draw(text)
            drawtext.text((base.width//3, base.height//4), content, font=font, fill=BLACK)
            icon.paste(avatar, (10, 10))
            image = images_alpha_composite(base, icon, text)
            return image