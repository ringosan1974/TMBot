import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

TRANSPARENT = (255, 255, 255, 0)
BLACK = (0, 0, 0, 255)