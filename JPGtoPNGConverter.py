#JPG to PNG Converter
# Better use PNG while developing a website
# receive two args  (folder name) 'Pokedex/'  'new/'

import sys
import os
from PIL import Image

current_path = os.getcwd()
#grab first & second args
file1 = sys.argv[1]
file2 = sys.argv[2]
filepath1 = current_path + file1
filepath2 = current_path + file2
file2Name = file2.replace('/','')

#check if new/exists, if not create it
if(os.path.isdir(filepath1)):
    if not(os.path.isdir(filepath2)):
        os.mkdir(file2Name)
#loop through Pokedex
    list = os.listdir(filepath1)
#convert to png
    for img in list:
        pngImg = img.replace('jpg','png')
        fp = filepath2+ '/' +pngImg #new folder path
        path = '.'+file1 + '/' +img
#save in new folder 
        im = Image.open(path)
        im.save(fp,'png')
else:
    print('wrong')


