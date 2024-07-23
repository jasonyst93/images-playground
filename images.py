from PIL import Image , ImageFilter

im = Image.open("./pokedex/pikachu.jpg")

#let's appying ImageFilter (BLUR)
filtered_img = im.filter(ImageFilter.BLUR)
#Save the blur image (Why png? It's because png support ImageFilter)
filtered_img.save("blur.png",'png')

#convert format 
grey_img = im.convert('L')
grey_img.save("grey.png",'png')

filtered_img.show()
im.show()
grey_img.show()

