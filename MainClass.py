from ImgCompositionClass import *
from ImgBasicsClass import *

class main():
    b = ImgBasics()
    boyImg = b.myReadImg('boy.jpg')
    b.myShowImg(boyImg)
    
    # Task 1 - image decomposition and recompostition
    c = ImgComposition()
    c.newGrid()
    boyImgPlanes = c.decompImg(boyImg)
    # b.myShowMultImg(boyImgPlanes)
    # plt.show()
    
    # Part c) - b.myShowMultImg

if __name__ == "__main__":
    main()