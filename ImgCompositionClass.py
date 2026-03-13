import cv2
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class ImgComposition():
    def __init__(self):
        print("Initialized image composition module")
    
    def helloIC(self):
        print("Hello image composition")
    
    # Display image
    def myShowImg(self, img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
    
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