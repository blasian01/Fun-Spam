import pyautogui
import time

time.sleep(5)

f = open("/Users/user1/folder/Fun-Spam/love.txt", 'r')
for line in f:
        pyautogui.typewrite(line)
        time.sleep(1) #used to limit time between messages
        pyautogui.press("enter")



          
        