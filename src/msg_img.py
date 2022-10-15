import disnake
import os


from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont


BACKGROUND = 'resources/background.jpg'
ICON = 'resources/icon.jpg'
FONT = 'resources/ShipporiMincho-Bold.ttf'
SAVEDFILE = 'resources/img.png'


class CreateMessageImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='msgimg', description='create image of message')
    async def messageimage(self, inter: disnake.ApplicationCommandInteraction, url: str):
        ids = self.__get_element_from_url(url)
        channel = await self.bot.fetch_channel(ids[0])
        message = await channel.fetch_message(ids[1])
        await self.__save_icon(message)
        self.__create_msgimg(message.content)
        await inter.response.send_message(file=disnake.File(SAVEDFILE))

    # make and save message-image
    def __create_msgimg(self, content: str):
        with Image.open(BACKGROUND).convert('RGBA') as base:
            with Image.open(ICON).convert('RGBA') as icon:
                font = ImageFont.truetype(FONT, 80)
                text = Image.new("RGBA", base.size, (255, 255, 255, 0))
                drawtext = ImageDraw.Draw(text)
                drawtext.text((base.width//3, base.height//4), content, font=font, fill=(0, 0, 0, 255))
                iconbase = Image.new("RGBA", base.size, (255, 255, 255, 0))
                iconbase.paste(icon, (10, 10))
                textbase = Image.alpha_composite(base, text)
                result = Image.alpha_composite(textbase, iconbase)
                result.save(SAVEDFILE)

    # get channel-id and message-id
    def __get_element_from_url(self, url: str):
        pearsed_url = url.split('/')
        return pearsed_url[-2:]  # message-id, channel-id

    # save user-icon from message object
    async def __save_icon(self, message: disnake.Message):
        await message.author.avatar.save(os.path.abspath(ICON))