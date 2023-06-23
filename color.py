from PIL import Image, ImageDraw, ImageFont

def color_box(size, color):
    img = Image.new('RGB', size, color)
    return img

def add_tex(image, text, font, font_color):
    W, H = image.size
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    draw.text(((W-w)/2, (H-h)/2), text, font=font, fill=fontColor)
    return image
