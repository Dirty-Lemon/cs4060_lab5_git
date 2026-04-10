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
    # def decompImg(self, img):
        # imgPlanes = []
        # # imgFloat = float(img)
        # # for i in range(0, 8):
        # #     imgPlanes.append(math.mod(math.floor(imgFloat / 2**i), 2))
        
        # imgWidth = img.shape[0]
        # imgHeight = img.shape[1]
        # pixels = []
        
        # for i in range(imgWidth):
        #     for j in range(imgHeight):
        #         pixels.append(np.binary_repr(img[i][j], imgWidth))
        
        # print("Image decomposed")
        # return imgPlanes
    
    # Decomposes image into bit-planes
    # Returns an array of 8 image planes decomposed from the image given as an argument
    def decompImg(self, img):        
        width = img.shape[0]
        height = img.shape[1]
        
        binary_pixel_list = []
        for i in range(width):
            for j in range(height):
                binary_pixel_list.append(np.binary_repr(img[i][j], width=8))
        
        bit0_img = (np.array([int(pixel[7]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit1_img = (np.array([int(pixel[6]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit2_img = (np.array([int(pixel[5]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit3_img = (np.array([int(pixel[4]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit4_img = (np.array([int(pixel[3]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit5_img = (np.array([int(pixel[2]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit6_img = (np.array([int(pixel[1]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        bit7_img = (np.array([int(pixel[0]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
        
        bit0_img = cv2.cvtColor(bit0_img, cv2.COLOR_BGR2RGB)
        bit1_img = cv2.cvtColor(bit1_img, cv2.COLOR_BGR2RGB)
        bit2_img = cv2.cvtColor(bit2_img, cv2.COLOR_BGR2RGB)
        bit3_img = cv2.cvtColor(bit3_img, cv2.COLOR_BGR2RGB)
        bit4_img = cv2.cvtColor(bit4_img, cv2.COLOR_BGR2RGB)
        bit5_img = cv2.cvtColor(bit5_img, cv2.COLOR_BGR2RGB)
        bit6_img = cv2.cvtColor(bit6_img, cv2.COLOR_BGR2RGB)
        bit7_img = cv2.cvtColor(bit7_img, cv2.COLOR_BGR2RGB)
        
        plt.subplot(241), plt.imshow(bit0_img), plt.title("bit0")
        plt.subplot(242), plt.imshow(bit1_img), plt.title("bit1")
        plt.subplot(243), plt.imshow(bit2_img), plt.title("bit2")
        plt.subplot(244), plt.imshow(bit3_img), plt.title("bit3")
        plt.subplot(125), plt.imshow(bit4_img), plt.title("bit4")
        plt.subplot(246), plt.imshow(bit5_img), plt.title("bit5")
        plt.subplot(247), plt.imshow(bit6_img), plt.title("bit6")
        plt.subplot(248), plt.imshow(bit7_img), plt.title("bit7")
        plt.show()