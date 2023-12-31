from PIL import Image, ImageDraw, ImageFont, ImageColor
import colorsys

def default_color_box(color, number=''):
    font = ImageFont.truetype('resources/Helvetica.ttf', 32)
    image = color_box((400,100), color)
    image = add_text(image, color, font, 'white', 'black', 3)
    image.save('resources/temp' + str(number) + '.png')

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

def im_cat(im1, im2):
    im1 = Image.open(im1)
    im2 = Image.open(im2)
    cat = Image.new('RGB', (im1.width, im1.height + im2.height))
    cat.paste(im1, (0, 0))
    cat.paste(im2, (0, im1.height))
    return cat

def RGB_to_HSV(color):
    r, g, b = color
    hsv = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    h, s, v = hsv
    h *= 360
    s *= 100
    v *= 100
    return (h, s, v)

def HSV_to_RGB(color):
    h, s, v = color
    rgb = colorsys.hsv_to_rgb(h/360, s/100, v/100)
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
    comHSV = ((180+h)%360, s, v)
    comRGB = HSV_to_RGB(comHSV)
    hex = RGB_to_HEX(comRGB)
    return(hex)

def triadic(color):
    rgb = ImageColor.getrgb(color)
    hsv = RGB_to_HSV(rgb)
    h, s, v = hsv
    tri1HSV = ((h + 120)%360, s, v)
    tri2HSV = ((h - 120)%360, s, v)
    tri1RGB = HSV_to_RGB(tri1HSV)
    tri2RGB = HSV_to_RGB(tri2HSV)
    hex1 = RGB_to_HEX(tri1RGB)
    hex2 = RGB_to_HEX(tri2RGB)
    return (hex1, color, hex2)
    
    
