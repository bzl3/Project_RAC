import win32api, win32con
import pyautogui
import time
 
def click(x,y):

        pyautogui.moveTo(x, y)
        pyautogui.click(clicks=3, interval=2)
	#win32api.SetCursorPos((400,465))
	#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def click():
        pyautogui.click()

for i in range (1,100):
        click()
        time.sleep(2)
