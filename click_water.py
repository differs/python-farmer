import pyautogui
import time

point = pyautogui.locateOnScreen('water.png')
click_point = pyautogui.center(point)

print(click_point)