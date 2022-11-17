# installation of pillow library
# change the image extension
# resize image files
# resize multiple image using for loop
# sharpness
# Brightness
# Color
# Contrast
# Image blur, GaussianBlur

from PIL import Image,ImageEnhance,ImageFilter

# img1 =Image.open('tree.jpg')
# img1.save('tree.pdf')     #------> change extension
# img1.show()

#--------------resize---------------
# max_size = (250,250)
# img1.thumbnail(max_size)
# img1.save('treeSmall.jpg')
# img2 =Image.open('treeSmall.jpg')
# img2.show()

#-----------using for loop for changing multiple image extension or resize----------
# import os
# for item in os.listdir():
#     if item.endswith('.jfif'):
#         img = Image.open(item)
#         filename, extension = os.path.splitext(item)
#         img.save(f'{filename}.png')



#-----------------------sharpness------------------------
# img1 =Image.open('tree.jpg')
# enhancer = ImageEnhance.Sharpness(img1)     # ImageEnhance--->module, Sharpness----> class of imageEnhance
# enhancer.enhance(3).save('tree1edited.jpg')
# 0: blurry
# 1: original image
# 2: sharpness increase

#-----------------------Color------------------------
# img1 =Image.open('tree.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save('tree1edited.jpg')

#-------------------Brightness---------------------

# img1 =Image.open('tree.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.5).save('tree1edited.jpg')

#-------------------Contrast---------------------

# img1 =Image.open('tree.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.5).save('tree1edited.jpg')

#-------------------Image blurr---------------------

img1 =Image.open('tree.jpg')
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('tree2edited.jpg')