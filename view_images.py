"""
Description:
    View images labelled with corresponding locations
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def visualise_data(img_file: str, location: str):
    # Show image and corresponding label
    imgplot = mpimg.imread(img_file)
    plt.imshow(imgplot)
    plt.title(location)
    plt.show()

def main():
    pass

if __name__ == "__main__":
    main()