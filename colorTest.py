from PIL import Image, ImageFont
import color as colour


font = ImageFont.truetype('resources/Helvetica.ttf', 32)
text = "test"

color = input("What color? ")
triadic = colour.triadic(color)


image1 = colour.color_box((200,100), triadic[0])
image2 = colour.color_box((200,100), color)
image3 = colour.color_box((200,100), triadic[1])

image1 = colour.add_text(image1, triadic[0], font, 'white', 'black', 3)
image2 = colour.add_text(image2, color, font, 'white', 'black', 3)
image3 = colour.add_text(image3, triadic[1], font, 'white', 'black', 3)

image1.save('resources/temp1.png')
image2.save('resources/temp2.png')
image3.save('resources/temp3.png')

colour.im_cat('resources/temp1.png', 'resources/temp2.png').save('resources/temp.png')
colour.im_cat('resources/temp.png', 'resources/temp3.png').save('resources/temp.png')
input()
