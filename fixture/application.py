# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
# from registration import Registration_data
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fixture.deposition import DepositionHelper
from fixture.session import SessinHelper
from fixture.katalog import KatalogHelper

class Application:

    def __init__(self, window_param = "--start-maximized"): #Конструктор 
        options = webdriver.ChromeOptions()
        options.add_argument(window_param)
        self.browser = webdriver.Chrome(chrome_options = options)
        self.browser.implicitly_wait(10)
        self.deposition = DepositionHelper(self)
        self.session = SessinHelper(self) #Ссылки на другие вспомогательные классы
        self.katalog = KatalogHelper(self) #Ссылки на другие вспомогательные классы
    
    def cookies(self):
        browser = self.browser
        all_cookies = browser.get_cookies()
        print(all_cookies)
        

    # def save_cookies(self):
    #     browser = self.browser
    #     pickle.dump(browser.get_cookies(), open("cokies.pkl", "wb"))
            
    # def give_cookies(self):
    #     browser = self.browser
    #     cookies = pickle.load(open("cookies.pkl","rb"))
    #     print(cookies) #смотрю что я загрузилось из дампа
    #     browser.delete_all_cookies()#выпилю старые прежде чем загрузить новые
    #     for cookie in cookies:
    #         browser.add_cookie(cookie)

    def open_page(self, url='http://devel.nris.ru/'):
        browser = self.browser
        browser.get(url)
        # self.assertIn("n'RIS", browser.title)
        # assert "n'RIS" in browser.title
        
          
    def profile_menu(self):
        # browser = self.browser
        # browser.find_elements_by_class_name("profile-menu").click() #не кликабельный элемент
        self.browser.find_element_by_xpath("//a[@class='header__user-link']").click()
        self.browser.find_element_by_link_text("Редактировать аккаунт").click()

    def destroy(self):
        self.browser.close()