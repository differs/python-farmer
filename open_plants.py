import pyautogui

point = pyautogui.locateOnScreen('plants.png')
click_point = pyautogui.center(point)
print(point)
print(click_point)

pyautogui.click(click_point)