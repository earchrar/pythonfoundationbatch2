from PIL import Image,ImageFilter

img = Image.open("./assets/e5.jpg")

print(img) # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=900x565 at 0x27046E76900>

print(img.format) # JPEG
print(img.size) # (900, 565)
print(img.mode) # RGB

filterimg = img.filter(ImageFilter.BLUR)
filterimg.save("newblurimg.png","png")

filterimg = img.filter(ImageFilter.SMOOTH)
filterimg.save("newsmoothimg.png","png")

filterimg = img.filter(ImageFilter.SMOOTH_MORE)
filterimg.save("newsmoothmoreimg.png","png")

filterimg = img.filter(ImageFilter.DETAIL)
filterimg.save("newdetailimg.png","png")

filterimg = img.filter(ImageFilter.EDGE_ENHANCE)
filterimg.save("newedgeenhanceimg.png","png")

filterimg = img.filter(ImageFilter.SHARPEN)
filterimg.save("newsharpenimg.png","png")

filterimg = img.filter(ImageFilter.CONTOUR)
filterimg.save("newcontourimg.png","png")

# -----------------------------------------------------------------------------------

# # => convert 
# filterimg = img.convert("L") # one parameter
# filterimg.save("newconvertimg.png","png") # black white 

# # => rotate 
# filterimg = img.convert("L")
# rotateimg = filterimg.rotate(-90) # one parameter
# rotateimg.save("newrotateimg.png","png") 

# # => resize 
# print(img.size) # (900, 565)
# resizeimg = img.resize((300,300)) # one parameter
# print(resizeimg.size) # (300, 300)
# resizeimg.save("newresizeimg.png","png")

# => thumbnail() , note : must be save with img 
# print(img.size) # (900, 565)
# img.thumbnail((300,300)) # one parameter
# print(img.size) # (300, 188)
# img.save("newthumbnail.png","png")

# => crop(left,upper,right,lower) 

# cpsize = (100,0,300,408) 
# print(img.size) # (300, 188)
# filterimg = img.crop(cpsize) # one parameter
# filterimg.save("newcropimg.png","png")
# print(filterimg.size) # (200, 408)








# https://pillow.readthedocs.io/en/stable/
# https://pypi.org/project/pillow/
# pip3 install pillow 
# pip3 show pillow