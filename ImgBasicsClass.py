# This class contains methods that are reused a lot in this course
import cv2

# Read image
class ImgBasics():
    def __init__(self):
        print("Initialized basic image methods")
        
    def myReadImg(self, imgName):
        imgPath = 'img/' + imgName      # All images will be in the img folder
        print("Reading " + imgName + "...")
        return cv2.imread(imgPath)
    
    # Display image
    def myShowImg(self, img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
    
    # Takes a 2D array of images to show on one display
    def showMultImg(self, imgsArray):
        print("Loading multiple images...")
        
        imgNum = 1
        for img in imgsArray:
            title = 'Image ' + str(imgNum)
            cv2.imshow(title, img)
            imgNum += 1
            
        cv2.waitKey(0)