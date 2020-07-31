import pyautogui
import time

x=1
while x<2:
    pyautogui.screenshot('/Users/Priya/Desktop/Python/image'+str(x)+'.png')
    x+=1
    time.sleep(2)