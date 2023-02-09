"""
Description:
    Script for creating the training split from msls dataset.

    Download the mapillary street level sequences dataset at:
        https://www.mapillary.com/dataset/places

    Download zipfile containing metadata and at least one zipfile
    containing a volume of images.
"""

import os
import cv2

BASE_DIR = "D:/mapillary/msls"

def read_image(img_filename: str):
    pass

def main():
    # Check which cities' images have been downloaded
    dirs = [f"{BASE_DIR}/train_val", f"{BASE_DIR}/test"]
    cities = {}
    for directory in dirs:
        for city in os.listdir(directory):
            image_dir = f"{directory}/{city}/query/images"
            if os.path.isdir(image_dir):
                cities[city] = image_dir
    if len(cities) == 0:
        exit("No images found. Exiting...")
    

if __name__ == "__main__":
    main()