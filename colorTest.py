from PIL import Image, ImageFont
import color as colour


font = ImageFont.truetype('resources/Helvetica.ttf', 32)
text = "test"

color = input("What color? ")
complement = colour.complement(color)

image1 = colour.color_box((200,100), color)
image2 = colour.color_box((200,100), complement)
image1 = colour.add_text(image1, text, font, 'white', 'black', 3)
image2 = colour.add_text(image2, text, font, 'white', 'black', 3)

image1.show()
image2.show()
input()
