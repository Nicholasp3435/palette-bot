from PIL import Image, ImageDraw, ImageFont
import color


font = ImageFont.truetype('resources/Helvetica.ttf', 32)
text = "test"

image = color.color_box((200,100), 'blue')

image = color.add_text(image, text, font, 'white', 'black', 3)

image.show()
input()
