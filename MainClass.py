from ImgCompositionClass import *
from ImgBasicsClass import *

class main():
    b = ImgBasics()
    # boyImg = b.myReadImg('boy.jpg')
    boyImg = cv2.imread('img/boy.jpg')
    cv2.imshow("Image", boyImg)
    cv2.waitKey(0)
    
    # Task 1 - image decomposition and recompostition
    c = ImgComposition()
    # c.newGrid()
    c.decompImg(boyImg)
    # b.myShowMultImg(boyImgPlanes)
    # plt.show()
    
    # Part c) - b.myShowMultImg

if __name__ == "__main__":
    main()