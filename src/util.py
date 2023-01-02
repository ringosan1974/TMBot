import disnake


from var import TRANSPARENT
from PIL import Image


# get channel-id and message-id
def get_ids_from(url: str):
    pearsed_url = url.split('/')
    return pearsed_url[-2:]  # message-id, channel-id


def images_alpha_composite(*args):
    result = Image.new('RGBA', args[0].size, TRANSPARENT)
    for i in args:
        result = Image.alpha_composite(result, i)
    return result


def get_user_name(member):
    return member.name if member.nick is None else member.nick