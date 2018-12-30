from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

webdriver = webdriver.Chrome()
webdriver.get('http://devel.nris.ru/')
all_cookies = webdriver.get_cookies()
print(all_cookies)