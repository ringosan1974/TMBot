from turtle import back
import disnake
import os


from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont
from var import TRANSPARENT, BLACK


BACKGROUND = 'resources/background.jpg'
ICON = 'resources/icon.jpg'
FONT = 'resources/ShipporiMincho-Bold.ttf'
SAVEDFILE = 'resources/img.png'


class CreateMessageImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='msgimg', description='create image of message')
    async def messageimage(self, inter: disnake.ApplicationCommandInteraction, url: str):
        ids = get_element_from_url(url)
        channel = await self.bot.fetch_channel(ids[0])
        message = await channel.fetch_message(ids[1])
        await save_icon(os.path.abspath(ICON), message)
        create_msgimg(BACKGROUND, ICON, message.content)
        await inter.response.send_message(file=disnake.File(SAVEDFILE))


# make and save message-image
def create_msgimg(background: str, avatar: str, content: str):
    with Image.open(background).convert('RGBA') as base:
        with Image.open(avatar).convert('RGBA') as iconimage:
            font = ImageFont.truetype(FONT, 80)
            text = Image.new("RGBA", base.size, TRANSPARENT)
            drawtext = ImageDraw.Draw(text)
            drawtext.text((base.width//3, base.height//4), content, font=font, fill=BLACK)
            icon = Image.new("RGBA", base.size, TRANSPARENT)
            icon.paste(iconimage, (10, 10))
            result = images_alpha_composite(base, icon, text)
            result.save(SAVEDFILE)

def images_alpha_composite(*args):
    result = Image.new('RGBA', args[0].size, TRANSPARENT)
    for i in args:
        result = Image.alpha_composite(result, i)
    return result

# get channel-id and message-id
def get_element_from_url(url: str):
    pearsed_url = url.split('/')
    return pearsed_url[-2:]  # message-id, channel-id

# save user-icon from message object
async def save_icon(fp: os.PathLike, message: disnake.Message):
    await message.author.avatar.save(fp)