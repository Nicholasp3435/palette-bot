from PIL import Image, ImageDraw, ImageFont, ImageColor
import colorsys

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

def RGB_to_HSV(color):
    r, g, b = color
    #Takes 255 values and normalizes
    hsv = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    #Return is normal
    return tuple(round(component, 2) for component in hsv)

def HSV_to_RGB(color):
    h, s, v = color
    rgb = colorsys.hsv_to_rgb(h, s, v)
    r, g, b, = rgb
    rgb = (int(r*255), int(g*255), int(b*255))
    return rgb

def RGB_to_HEX(color):
    r, g, b = color
    r = f'{r:02x}'
    g = f'{g:02x}'
    b = f'{b:02x}'
    return("#" + r + g + b)


def complement(color):
    rgb = ImageColor.getrgb(color)
    hsv = RGB_to_HSV(rgb)
    h, s, v = hsv
    comHSV = ((0.5+h)%1, s, v)
    comRGB = HSV_to_RGB(comHSV)
    hex = RGB_to_HEX(comRGB)
    return(hex)
