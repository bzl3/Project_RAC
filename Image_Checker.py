from PIL import Image
import pytesseract

class Image_Checker:

    def __init__(self):
        train_cnt = 0
        th = 0
        
    # need to train pytesseract!!!
    def print_str_from_img( self, path ):
        try:
            im = Image.open(path)
            result = pytesseract.image_to_string(im)
        except:
            print ("Failed to convert img to str")
            return None
        print(result)
        return result

    
    def get_main_color( self, im ):
        h = im.histogram()
        red = 0
        green = 0
        blue = 0

        # split into red, green, blue
        r = h[0:256]
        g = h[256:256*2]
        b = h[256*2: 256*3]

        for i,w in enumerate(r):
            red = red + i*w
        for i,w in enumerate(g):
            green = green + i*w
        for i,w in enumerate(b):
            blue = blue + i*w
            
        if ( red > blue and red > green ):
            #print("Main color is RED!")
            return 'r'
        elif ( blue > red and blue > green ):
            #print("Main color is BLUE!")
            return 'b'
        elif ( green > red and green > blue ):
            #print("Main color is GREEN!")
            return 'g'
        else:
            print("Failed to find main color")
            return 'n'

    
