#!/usr/bin/env python3

import os
import PIL

img_path = 'catalog-updater/supplier-data/images'
new_dir = 'supplier-data/converted'


# if not os.path.exists(new_dir):
#     os.makedirs(new_dir)


for img in os.listdir(img_path):
    if (img.endswith('.tiff')):
        print(img)
