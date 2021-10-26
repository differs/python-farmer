import pyautogui
import time

# im1 = pyautogui.screenshot('good.png')

# button8_location = pyautogui.locateOnScreen('8.png')
# print(button8_location)

def add_power():
    # point = pyautogui.locateOnScreen('add_power.png')
    # print(point)
    # if point != None:
    #     click_point = pyautogui.center(point)
    #     print(click_point)
    # pyautogui.click('addenrgy.png')
    # button7point = pyautogui.center(button7location)
    
    # x,y = pyautogui.Point()

    for i in range(0,10):
        i += 1
        pyautogui.click(x=1090, y=569)
        print("add_power")
    # pyautogui.moveTo(150,150)


def confirm_add_power():
    time.sleep(3)
    pyautogui.click(x=963, y=638)
    print("confirm add power")
    time.sleep(3)
    # point = pyautogui.locateOnScreen('add_power_exchange_on.png')
    # if point != None:
    #     click_point = pyautogui.center(point)
    #     print(click_point)
    #     pyautogui.click(click_point)

def open_add_power():
    pyautogui.click(x=1508, y=295)
    pyautogui.moveTo(200, 200)

    # point = pyautogui.locateOnScreen('open_add_power.png')
    # if point != None:
    #     # click_point = pyautogui.center(point)
    #     # print(point[0] + point[2], point[1] - point[3] / 2)
    #     # click_point = (point[0] + point[2], point[1] / 2 + point[3] / 2)
    #     # pyautogui.click(point[0], point[1] + point[3] / 2)
    #     click_point = pyautogui.center(point)
    #     pyautogui.click(click_point)
    #     pyautogui.moveTo(100, 100)
    #     time.sleep(2)

def water_add():
    point = pyautogui.locateOnScreen('water.png')
    if point != None:
        click_point = pyautogui.center(point)
        print(click_point)
        print("checking water")
        pyautogui.click(click_point)
        time.sleep(5)

def open_map():
    pyautogui.click(x=1082, y=883)
    time.sleep(2)
    # point = pyautogui.locateOnScreen('open_map.png')
    # print(point)
    # if point != None:
    #     click_point = pyautogui.center(point)
    #     pyautogui.click(click_point)

def open_plant():
    pyautogui.click(x=764, y=701)
    time.sleep(2)
    # point = pyautogui.locateOnScreen('open_plant.png')
    # if point != None:
    #     click_point = pyautogui.center(point)
    #     pyautogui.click(click_point)
    #     time.sleep(1)
    water_everplants()


def water_everplants():
    pyautogui.click(723,444)
    time.sleep(1)
    pyautogui.scroll(+800)
    time.sleep(2)

    pyautogui.click(723,444 + 8)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83 + 8 )
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83+83 + 8)
    time.sleep(2)
    water_add()

    pyautogui.click(723,444+83+83+83 + 8)
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
    if pyautogui.locateOnScreen('cancel.png') !=None and pyautogui.locateOnScreen('cancel.png'):
        pyautogui.click('cancel.png')

def water_operate():
    print("open map")
    open_map()
    time.sleep(2)

    print("open plants")
    open_plant()
    time.sleep(1)
    print("add water")
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

