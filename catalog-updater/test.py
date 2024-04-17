import os
from PIL import Image

img_path = 'catalog-updater/supplier-data/images'

for files in os.listdir(img_path):
    if files.endswith('tiff'):
        os.remove(files)