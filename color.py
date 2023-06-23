from PIL import Image, ImageDraw, ImageFont

def color_box(size, color):
    img = Image.new('RGB', size, color)
    return img

def add_text(image, text, font, font_fg_color, font_bg_color, stroke_width):
    W, H = image.size
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    draw.text(((W-w)/2, (H-h)/2), text, font=font, fill=font_bg_color,
              stroke_fill = font_fg_color, stroke_width = stroke_width)
    return image
