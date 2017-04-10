from PIL import ImageGrab
from Screen_Module import Screen_Module
from Image_Checker import Image_Checker

if __name__ == "__main__":
    img_path = "bot1.jpg"
    sm = Screen_Module()
    ic = Image_Checker()
    sm.init_box_coordinate();
    
    # part of the screen
    im = sm.grab()
    im.save(img_path, "JPEG")
#    im.show()
    result = ic.print_str_from_img( img_path )
