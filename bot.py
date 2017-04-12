from PIL import ImageGrab
from Screen_Module import Screen_Module
from Image_Checker import Image_Checker
from Mail_module import Mail_module
from datetime import datetime
import time
import winsound

if __name__ == "__main__":
    server = 'smtp.gmail.com:587'
    username = input("Enter bot mail username: ")
    pw = input("Enter pw: ")
    to_addr = input("Enter recipient email: ")
    mm = Mail_module( username, pw, server )
    mm.set_from("RAC Bot")
    
    sm = Screen_Module()
    ic = Image_Checker()
    sm.init_box_coordinate();
    t = 5;
    sent = False

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
            #winsound.PlaySound("barking.wav", winsound.SND_FILENAME)
            t = 5
        elif('b' == color ):
            print("%s : Hippo is doing OK" %(str(datetime.now())))
            sent = False
            t = 10
        else:
            print("What happen?????")

        time.sleep(t)
        
    
