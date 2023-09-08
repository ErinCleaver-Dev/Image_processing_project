# writing scripts to have them do something for us
# What instagram dose is it processes the image
# crops the image and makes it small
# save money by compressing the video
# https://pillow.readthedocs.io/en/stable/

#Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL.
#Allows python 3 support

from PIL import Image, ImageFilter

# img = Image.open('.\pokedex\pikachu.jpg')
# print(img.format)
# print(img.size)

# print(img.mode)

# # runs the blur filter on the image
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save(".\pokedex\edited\\blured_pikachu.png", "png")
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save(".\pokedex\edited\\smooth_pikachu.png", "png")
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save(".\pokedex\edited\\sharpen_pikachu.png", "png")

# #to convert the image
# converted = img.convert('L')
# #routes the image
# converted.save(".\pokedex\edited\\gray_pikachu.png", "png")
# #print(dir(img))

# #to open the image
# # converted.show()

# #must have a tuple 
# resize = img.resize((300, 300))
# resize.save(".\pokedex\edited\\thum_nail.png", "png")
# # resize.show()

# box = (40, 40, 400, 400)
# cropped_image = img.crop(box)
# cropped_image.save(".\pokedex\edited\\cropped_image.png", "png")
# cropped_image.show()

img = Image.open('.\character design 1.png')
print(img.size)
img.thumbnail((400, 200))
resized_image = img.convert('RGB')
resized_image.save('resized_image.jpg')
print(resized_image.size)