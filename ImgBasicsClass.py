import cv2

# This class contains methods that are reused a lot in this course
class ImgBasics():
    def __init__(self):
        print("Initialized basic image methods")
    
    # Converts image into a cv2-readable format
    # Returns an array readable as a cv2 image
    def myReadImg(self, imgName):
        imgPath = 'img/' + imgName      # All images will be in the img folder
        print("Reading " + imgName + "...")
        return cv2.imread(imgPath)
    
    # Display image
    # Takes an image that has been converted in the myReadImg function 
    def myShowImg(self, img):
        print("Loading image...")
        cv2.imshow("Image", img)
        cv2.waitKey(0)
    
    # Takes a 2D array of images to show on one display
    def myShowMultImg(self, imgsArray):
        print("Loading" + len(imgsArray) + " images...")
        
        imgNum = 1
        for img in imgsArray:
            title = 'Image ' + str(imgNum)
            cv2.imshow(title, img)
            imgNum += 1
            
        cv2.waitKey(0)