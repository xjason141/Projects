#!/usr/bin/python3

import os
from PIL import Image

#new dir for formatted images
new_dir = r'opt/icons/'

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

#formatting begins here
for img in os.listdir('pics/'):
    if img != '.DS_Store': #skips '.DS_Store' file
        name = img.split("/")[-1]

        with Image.open('pics/' + img) as pic: #syntax here is == ('pics/<imageName>')
            
            #Current size and format
            # print('Current size is: ' + str(pic.size))
            # print('Current format is: ' + str(pic.format))

            new_pic = pic.resize((128,128)).rotate(-90).convert('RGB')
            print('Processing ' + str(img) + '...')
            new_pic.save(new_dir + name + '.jpeg')

