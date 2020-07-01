#!/usr/bin/env python3

# 1. resize and convert images in folder from .tiff to .jpeg
from PIL import Image
import os

folder = "supplier-data/images/"

for root, _, files in os.walk(folder):
    for filename in files:
        if '.tiff' in filename:
            filename, ext = filename.split('.')
            print(root, filename, ext)
            with Image.open(root+filename+'.'+ext) as img:
                img = img.convert('RGB')
                img = img.resize((600, 400))
                img.save(root+filename+'.jpeg')
