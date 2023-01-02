import disnake
import random


from disnake.ext import commands


class Omikuji(commands.Cog):
    fortunes = ("大吉", "中吉", "小吉", "凶", "大凶")
    lucky_things = ("赤", "青", "水色", "黄色", "緑", "黒", "白", "お姉ちゃんの靴", "靴を舐める", "イヤホン", "女声を出す")

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def omikuji(self, inter):
        fortune = random.choice(self.fortunes)
        lucky_thing = random.choice(self.lucky_things)
        await inter.response.send_message(f"あなたは{fortune}です！\nラッキーなものは{lucky_thing}です！")