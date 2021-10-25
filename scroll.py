import pyautogui
import time

# 83 px down
# Point(x=723, y=444)
# Point(x=723, y=527)
# point_1 = pyautogui.locateOnScreen('seed_1.png')

# point_2 = pyautogui.locateOnScreen('seed_2.png')

# click_1 = pyautogui.center(point_1)

# click_2 = pyautogui.center(point_2)

# print(click_1, click_2)

# print(click_1)
# print(click_2)

pyautogui.click(723,444)
time.sleep(1)


pyautogui.click(723,444)
time.sleep(2)
pyautogui.click(723,444+83)
time.sleep(2)
pyautogui.click(723,444+83+83)
time.sleep(2)
pyautogui.click(723,444+83+83+83)

pyautogui.scroll(-400)
time.sleep(2)

pyautogui.click(723,444)
time.sleep(2)
pyautogui.click(723,444+83)
time.sleep(2)
pyautogui.click(723,444+83+83)
time.sleep(2)
pyautogui.click(723,444+83+83+83)

