import pyautogui
import time

time.sleep(5)

f = open("text.txt", 'r')
for line in f:
        pyautogui.typewrite(line)
        time.sleep(2)
        pyautogui.press("enter")