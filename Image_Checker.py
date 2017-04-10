from PIL import Image
import pytesseract

class Image_Checker:

    def __init__(self):
        train_cnt = 0
        th = 0
        

    def print_str_from_img( self, path ):
        try:
            im = Image.open(path)
#        im.show()
            result = pytesseract.image_to_string(im)
        except:
            print ("Failed to convert img to str")
            return None
        print(result)
        return result
    

            
