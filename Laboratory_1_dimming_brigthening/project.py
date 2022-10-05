import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read and show the image:
img = cv2.imread('resources\\terrain_map_01.jpg')
plt.imshow(img)
plt.show()

# Grid and 3D greyscale plot of the image:
xx, yy = np.mgrid[0:img.shape[0], 0:img.shape[1]]
fig = plt.figure()
ax = fig.gca()
ax = fig.add_subplot(111, projection='3d')
plt.show()



