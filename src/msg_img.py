import disnake


from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont


class CreateMessageImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='msgimg', description='create image of message')
    async def messageimage(self, inter: disnake.ApplicationCommandInteraction, url: str):
        # message = get_msgid_from_url(url)
        await inter.response.send_message(url)
        # image = create_image(message)
        # send image

    # todo: understand how to use pillow.
    def create_image(self, word: str):
        with Image.open('images/background137.jpg').convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', 80)
            draw = ImageDraw.Draw(txt)
            draw.text((877, 310), word, font=font, fill=(0, 0, 0, 255))
            out = Image.alpha_composite(base, txt)
            out.show()

    def get_msgid_from_url(url: str):
        # parse url and get message id.
        pass
