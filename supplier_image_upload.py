#!/usr/bin/env python3

# 2. upload images from folder to url

import requests
import os

folder = 'supplier-data/images/'
url = 'http://localhost/upload/'
counter = 0
for root, _, files in os.walk(folder):
    for filename in files:
        if '.jpeg' in filename:
            with open(root+filename, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
                counter += 1
print(counter, 'items uploaded')
