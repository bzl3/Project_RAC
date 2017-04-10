from PIL import ImageGrab
import msvcrt
import win32gui

class Screen_Module:
    
    def __init__(self):
        self.init = False
        self.x = 0
        self.y = 0
        self.x1 = 0
        self.y1 = 0

    def get_point(self):
        ret = True

        while ret:
            c = msvcrt.getwch()
            if "c" == c:
                ret = False
            
        (tmpX,tmpY) = win32gui.GetCursorPos()
        return tmpX, tmpY


    def init_box_coordinate(self):
        print ("Place mouse to top left of box, and press key \"c\"")
        self.x, self.y = self.get_point()
        print ("Place mouse to bottom right of box, and press key \"c\"")
        self.x1, self.y1 = self.get_point()

        print("(X,Y) = (%d, %d), (X1,Y1) = (%d, %d)" %(self.x, self.y, self.x1, self.y1))
        self.init = True

    def grab(self):
        if (not self.init):
            print("Not initalized yet")
        else:
            im=ImageGrab.grab(bbox=(self.x,self.y,self.x1,self.y1))
        return im
