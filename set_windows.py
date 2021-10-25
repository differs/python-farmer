# import webbrowser
# firefox = webbrowser.get("firefox")
# firefox.open("https://baidu.com")

# firefox.open_new_tab("https://taobao.com")

import selenium
from selenium import webdriver


url = "https://baidu.com"

driver = webdriver.Chrome()
print(driver.Options.arguments)
driver.set_window_size(800, 600)
driver.get(url)
# ChromeOptions options = new ChromeOptions()

# options.add_argument("-incognito -window-size=1366, 768 -disable-infobars")