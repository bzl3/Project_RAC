from PIL import ImageGrab
from Screen_Module import Screen_Module
from Image_Checker import Image_Checker
from Mail_module import Mail_module
from datetime import datetime
import time
import winsound
import pyautogui
import msvcrt

def click(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def get_point():
    ret = True
    while ret:
        c = msvcrt.getwch()
        if "c" == c:
            ret = False
    return pyautogui.position()

if __name__ == "__main__":
    server = 'smtp.gmail.com:587'
    username = input("Enter bot mail username: ")
    pw = input("Enter pw: ")
    to_addr = input("Enter recipient email: ")
    mm = Mail_module( username, pw, server )
    mm.set_from("RAC Bot")
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    sm = Screen_Module()
    ic = Image_Checker()
    sm.init_box_coordinate();
    t = 5;
    sent = False
    print("Place mouse on 1st point and press key \"c\"");
    (x1,y1) = get_point();
    print("Place mouse on 2st point and press key \"c\"");
    (x2,y2) = get_point();

    while (True):
        im = sm.grab()
        color = ic.get_main_color(im)
        if ( 'n' == color ):
            break
        elif('r' == color ):
            print( "%s : Hippo is HUNGRY!!!!" %(str(datetime.now())))
            if ( not sent ):
                mm.sendmail(to_addr, "Hippo's hungry!", str(datetime.now()))
                sent = True
            click(x1, y1)
            time.sleep(2)
            click(x2, y2)
            t = 5
        elif('b' == color ):
            print("%s : Hippo is doing OK" %(str(datetime.now())))
            sent = False
            t = 10
        else:
            print("What happen?????")

        time.sleep(t)
        
    
