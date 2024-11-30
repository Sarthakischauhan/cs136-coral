#! base/bin/python3

import os

def get_all_files(directory):
    all_images = []
    for root, dirs,files in os.walk(directory):
        for file in files:
            if file.endswith("JPG"):
                all_images.append(os.path.join(root, file))
    return all_images

    