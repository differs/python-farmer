import pyautogui
import time

# point = pyautogui.locateOnScreen('open_add_power.png')
# # point.l

# print(point)
# print(point[0],point[1],point[2],point[3])
# print(point[0] + point[2], point[1] / 2 + point[3] / 2)


point = pyautogui.locateOnScreen('power_button.png')

print(point)

click_point = pyautogui.center(point)

print(click_point)