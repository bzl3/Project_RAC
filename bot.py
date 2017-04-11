from PIL import ImageGrab
from Screen_Module import Screen_Module
from Image_Checker import Image_Checker
from datetime import datetime
import time
import winsound

if __name__ == "__main__":
    img_path = "bot1.jpg"
    sm = Screen_Module()
    ic = Image_Checker()
    sm.init_box_coordinate();
    t = 5;
    
    # part of the screen
    #im.save(img_path, "JPEG")
    #im.show()
    #result = ic.print_str_from_img( img_path )
    
    while (True):
        im = sm.grab()
        color = ic.get_main_color(im)
        if ( 'n' == color ):
            break
        elif('r' == color ):
            print( "%s : Hippo is HUNGRY!!!!" %(str(datetime.now())))
            winsound.PlaySound("barking.wav", winsound.SND_FILENAME)
            t = 5
        elif('b' == color ):
            print("Hippo is doing OK")
            t = 30
        else:
            print("What happen?????")

        time.sleep(t)
        
    
