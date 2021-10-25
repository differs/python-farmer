import pyautogui
import time

# im1 = pyautogui.screenshot('good.png')

# button8_location = pyautogui.locateOnScreen('8.png')
# print(button8_location)

def add_power():
    point = pyautogui.locateOnScreen('add_power.png')
    print(point)
    if point != None:
        click_point = pyautogui.center(point)
        print(click_point)
    # pyautogui.click('addenrgy.png')
    # button7point = pyautogui.center(button7location)
    
    # x,y = pyautogui.Point()
        for i in range(0,10):
            i += 1
            pyautogui.click(click_point)
            print("add_power.png")
        pyautogui.moveTo(50,50)


def confirm_add_power():
    point = pyautogui.locateOnScreen('add_power_exchange_on.png')
    if point != None:
        click_point = pyautogui.center(point)
        print(click_point)
        pyautogui.click(click_point)

def open_add_power():
    point = pyautogui.locateOnScreen('open_add_power.png')
    if point != None:
        # click_point = pyautogui.center(point)
        print(point[0] + point[2], point[1] - point[3] / 2)
        # click_point = (point[0] + point[2], point[1] / 2 + point[3] / 2)
        pyautogui.click(point[0], point[1] + point[3] / 2)

def water_add():
    point = pyautogui.locateOnScreen('water.png')
    if point != None:
        click_point = pyautogui.center(point)
        print(click_point)
        print("checking water")
        pyautogui.click(click_point)
        time.sleep(5)

def open_map():
    point = pyautogui.locateOnScreen('open_map.png')
    if point != None:
        click_point = pyautogui.center(point)
        pyautogui.click(click_point)

def open_plant():
    point = pyautogui.locateOnScreen('open_plant.png')
    if point != None:
        click_point = pyautogui.center(point)
        pyautogui.click(click_point)
        time.sleep(1)
        water_everplants()


def water_everplants():
    pyautogui.click(723,444)
    time.sleep(1)

    pyautogui.click(723,444)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83+83)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83+83+83)
    time.sleep(1)
    water_add()

    pyautogui.scroll(-400)
    time.sleep(2)


    pyautogui.click(723,444)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83+83)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83+83+83)
    time.sleep(2)
    water_add()


# def open_cow_shed():


# def open_mining():

def power_full():
    if pyautogui.onScreen('exchange_grey.png') or pyautogui.onScreen('cancel.png'):

        if pyautogui.locateOnScreen('cancel.png') !=None:

            pyautogui.click('cancel.png')

def water_operate():
    open_map()
    time.sleep(2)
    open_plant()
    time.sleep(1)
    water_add()
    time.sleep(1)

def power_operate():
    open_add_power()
    print("打开体力窗口")
    time.sleep(2)

    add_power()
    print("加满")
    time.sleep(2)

    confirm_add_power()
    print("确认")
    time.sleep(2)

    power_full()
    print("power full")



def main():
    while True:
       
        power_operate()

        water_operate()
        print("准备加水")
        time.sleep(1)
    

main()

