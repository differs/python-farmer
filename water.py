import pyautogui
import time

def water_add():
    point = pyautogui.locateOnScreen('water.png')
    if point != None:
        click_point = pyautogui.center(point)
        print(point)
        print(click_point)
        print("checking water")
        # pyautogui.click(click_point)
        time.sleep(5)


water_add()