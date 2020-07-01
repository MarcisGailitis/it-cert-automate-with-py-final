#! /usr/bin/env python3

# 3. upload descriptions from folder to url

import os
import requests

folder = 'supplier-data/descriptions/'
d_keys = ['name', 'weight', 'description', 'image_name']
url = 'http://104.154.91.216/fruits/'

for root, _, files in os.walk(folder):
        for filename in files:
            # print(root, filename)
            out_dict = {}
            with open(root+filename, 'r') as description:
                for line, content in enumerate(description):
                    # create a dictionary out_dict with
                    # keys from d_keys and values from description file content

                    # take line 0 and line 2 and add it to dict
                    if line == 0 or line == 2:
                        out_dict[d_keys[line]] = content.replace('\n', '')

                    # remove lbs from 1st line
                    if line == 1:
                        out_dict[d_keys[line]] = content[:content.index(' ')]

                # add image name to out_dict, filename.txt -> filename.jpeg
                out_dict[d_keys[3]] = filename[:filename.index('.')]+'.jpeg'

            response = requests.post(url, data=out_dict)
            print(response.status_code)
