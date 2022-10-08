import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read and show the image:
img = cv2.imread('resources\\terrain_map_01.jpg')
plt.imshow(img)
plt.show()

# Function for brightening:
def threshold(img, thresh=200):
        return((img > thresh) * 255).astype("uint8")

# Function for dimming:
def reverse_threshold(img, thresh=200):
        return((img < thresh) * 255).astype("uint8")

# Usage:
plt.imshow(threshold(img), cmap='gray')
plt.show()
plt.imshow(reverse_threshold(img), cmap='gray')
plt.show()


