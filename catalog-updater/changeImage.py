#!/usr/bin/env python3

import os
from PIL import Image

img_path = 'catalog-updater/supplier-data/images'
# new_dir = r'catalog-updater/supplier-data/converted/'
save_point = 'catalog-updater/supplier-data/images/'


if not os.path.exists(save_point):
    os.makedirs(save_point)


for img in os.listdir(img_path):
    if (img.endswith('.tiff')):
        name = img[:-4]

        with Image.open(img_path + '/' + img) as pics:
            new_pic = pics.resize((600,400)).convert('RGB')
            print('Processing ' + str(img) + '...')
            new_pic.save(save_point + name + 'jpeg')