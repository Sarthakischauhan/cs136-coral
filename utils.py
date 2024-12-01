#! base/bin/python3

import os

def get_all_files(directory):
    """
    Will return the list of file names from the directory that are of .jpg type
    """
    all_images = []
    for root, dirs,files in os.walk(directory):
        for file in files:
            if file.endswith("JPG") or file.endswith("jpg"):
                all_images.append(os.path.join(root, file))
    return all_images
