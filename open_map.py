import pyautogui

point = pyautogui.locateOnScreen('open_map.png')
click_point = pyautogui.center(point)
print(point)
print(click_point)
pyautogui.click(click_point)
pyautogui.click(click_point)