from PIL import Image , ImageFilter

new_image = Image.open("./astro.jpg")
print(new_image.size)

new_image = new_image.resize((400,200))
new_image.save('thumbnail.jpg')
print(new_image.size)

#It looks weired... How can we keep the aspect ratio
thumbnail =Image.open("./astro.jpg")
thumbnail.thumbnail((400,400)) #  giving maxium within - 400 x 400 
thumbnail.save('thumbnail_2.jpg')

print(thumbnail.size)
#Useful to create profile picture