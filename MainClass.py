from ImgCompositionClass import *
from ImgBasicsClass import *

class main():
    b = ImgBasics()
    # boyImg = b.myReadImg('boy.jpg')
    boyImg = cv2.imread('img/boy.jpg')
    b.myShowImg(boyImg)
    
    # Task 1 - image decomposition and recompostition
    c = ImgComposition()
    # c.newGrid()
    c.decompImg(boyImg)
    # b.myShowMultImg(boyImgPlanes)
    # plt.show()
    
    # Part c) - b.myShowMultImg
    
    # Task 2 - Histogram Equalization
    lena_img = cv2.imread('img/lena.tif')
    b.myShowImg(lena_img)

if __name__ == "__main__":
    main()