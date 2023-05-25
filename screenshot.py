from pyautogui import *
import pyautogui
import keyboard


KEYBOARD_TO_PRESS = 'f2'
DIRECTORY_AND_FILE_NAME = './savedimage.png'


keyboard.wait(KEYBOARD_TO_PRESS)
coor1 = pyautogui.position()
print("Coor 1 : " + str(coor1.x) + " " + str(coor1.y))

keyboard.wait(KEYBOARD_TO_PRESS)
coor2 = pyautogui.position()
print("Coor 2 : " + str(coor2.x) + " " + str(coor2.y))

im1 = pyautogui.screenshot(region=(coor1.x,coor1.y,coor2.x-coor1.x,coor2.y-coor1.y))
im1.save(DIRECTORY_AND_FILE_NAME)
print("Image saved!")
