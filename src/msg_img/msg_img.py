from PIL import Image, ImageDraw, ImageFont

# get an image
with Image.open('images/background137.jpg').convert("RGBA") as base:
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', 80)
    d = ImageDraw.Draw(txt)
    d.text((877, 310), "HelloWorld", font=fnt, fill=(0, 0, 0, 255))
    out = Image.alpha_composite(base, txt)
    out.show()
