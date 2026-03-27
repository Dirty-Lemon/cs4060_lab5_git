import cv2
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

# This class contains methods used mainly in assignment 5
class ImgComposition():
    def __init__(self):
        print("Initialized image composition module")
    
    # Create a grid with 2 rows and 4 columns
    def newGrid(self):
        fig = plt.figure()
        plt.suptitle("Image")
        
        # Create 8 subplots in a 2 x 4 configuration
        nrows = 2
        ncols = 4
        nFigs = 8
        for i in range(0, nFigs):
            axis = fig.add_subplot(nrows, ncols, 1 + i)
            axis.title.set_text('Bit-Plane ' + str(i))
        
        plt.setp(plt.gcf().get_axes(), xticks = [], yticks = [])    # Removes all axis labels
        # plt.grid(True)
        plt.show()
    
    # Decomposes image into bit-planes
    # Returns an array of 8 image planes decomposed from the image given as an argument
    def decompImg(self, img):
        imgPlanes = []
        # imgFloat = float(img)
        # for i in range(0, 8):
        #     imgPlanes.append(math.mod(math.floor(imgFloat / 2**i), 2))
        
        imgWidth = img.shape[0]
        imgHeight = img.shape[1]
        pixels = []
        
        for i in range(imgWidth):
            for j in range(imgHeight):
                pixels.append(np.binary_repr(img[i][j], imgWidth))
        
        print("Image decomposed")
        return imgPlanes