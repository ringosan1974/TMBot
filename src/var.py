import os


from dotenv import load_dotenv
from enum import Enum
from PIL import Image


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


TRANSPARENT = (255, 255, 255, 0)
BLACK = (0, 0, 0, 255)
BACKGROUND = 'resources/background.jpg'
FONT = 'resources/ShipporiMincho-Bold.ttf'


class Words(Enum):
    TWO = '２か。。。ハズレだ'
    THREE = '良い判断だキルア　そのままゴンを連れて逃げろ　それまでは時間を稼ぐ！！'
    FOUR = 'もういい　消えろ'
    CRAZYSLOT = '口の中にルーレット!! 数字は１から９ 出た目によって武器が変わる!!\nそれがオレ様"気狂いピエロ"さ!!\nいい目が出ろよ!!\n'