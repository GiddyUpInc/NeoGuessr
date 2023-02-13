"""
Description:
    Script for creating the training split from msls dataset.

    Download the mapillary street level sequences dataset at:
        https://www.mapillary.com/dataset/places

    Download zipfile containing metadata and at least one zipfile
    containing a volume of images. Extract all zip files to same 
    parent directory and specify location as BASE_DIR below.
"""

import os
import cv2
import numpy as np
import pandas as pd

IMG_SIZE = 64

BASE_DIR = "D:/mapillary/msls"

def read_image(img_filename: str) -> np.ndarray:
    """Read image and return as numpy array"""
    img_array = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)
    img_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
    return img_array

def main():
    # Check which cities' images have been downloaded
    dirs = [f"{BASE_DIR}/train_val", f"{BASE_DIR}/test"]
    cities = {}
    for directory in dirs:
        for city in os.listdir(directory):
            city_dir = f"{directory}/{city}"
            if os.path.isdir(f"{city_dir}/query/images"):
                cities[city] = city_dir
    if len(cities) == 0:
        exit("No images found. Exiting...")
    # Load images into a dataset with a label indicating their location
    img_data = []
    for city, dir_name in cities.items():
        img_dir = f"{dir_name}/query/images"
        seq_info = pd.read_csv(f"{dir_name}/query/seq_info.csv")
        for i in range(seq_info.shape[0]):
            key = seq_info.at[i, "key"]
            seq_key = seq_info.at[i, "sequence_key"]
            img = read_image(f"{img_dir}/{key}.jpg")
            img_data.append([img, city, seq_key])
        break
    print(len(img_data), seq_info.shape[0])

if __name__ == "__main__":
    main()