#!/usr/bin/env python3

import os
from PIL import Image

img_path = 'catalog-updater/supplier-data/images'
new_dir = r'catalog-updater/supplier-data/converted/'


if not os.path.exists(new_dir):
    os.makedirs(new_dir)


for img in os.listdir(img_path):
    if (img.endswith('.tiff')):
        name = img[:-4]

        with Image.open(img_path + '/' + img) as pics:
            new_pic = pics.resize((600,500)).convert('RGB')
            print('Processing ' + str(img) + '...')
            new_pic.save(new_dir + name + '.jpeg')