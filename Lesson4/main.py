from PIL import Image

length = 50
image = Image.open("monro.jpg")
red, green, blue  = image.split()

coordinates = (length, 0, red.width, red.height)
cropped1 = red.crop(coordinates)
coordinates = (length/2, 0, red.width-length/2, red.height)
cropped2 = red.crop(coordinates)
image_red = Image.blend(cropped1, cropped2, 0.2)

coordinates = (0, 0, blue.width-length, blue.height)
cropped1 = blue.crop(coordinates)
coordinates = (length/2, 0, blue.width-length/2, blue.height)
cropped2 = blue.crop(coordinates)
image_blue = Image.blend(cropped1, cropped2, 0.2)

coordinates = (length/2, 0, green.width-length/2, green.height)
image_green = green.crop(coordinates)
 
new_image = Image.merge("RGB", (image_red,image_green, image_blue ))
new_image.save("Warhol.jpg")
new_image.thumbnail((80, 80)) 
new_image.save("Avatar.jpg")
