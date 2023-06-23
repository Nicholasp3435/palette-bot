from PIL import Image, ImageFont
import color


font = ImageFont.truetype('resources/Helvetica.ttf', 32)
text = "test"

image = color.color_box((200,100), 'blue')
image = color.add_text(image, text, font, 'white', 'black', 3)

print(color.complement("cyan"))


image.show()
input()
