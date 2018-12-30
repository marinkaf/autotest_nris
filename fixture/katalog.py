# -*- coding: utf-8 -*-

import time

class KatalogHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        browser = self.app.browser
        elem_menu_catalog = browser.find_element_by_link_text("Мой каталог")
        elem_menu_catalog.click()
        time.sleep(5)
        elem_submenu_catalog_AditAndPay = browser.find_element_by_link_text("Обработка и описание")
        elem_submenu_catalog_AditAndPay.click()

    def find_file_AditAndPay(self):
        browser = self.app.browser
        # browser.find_element_by_class_name("files-editor-files").click()
        # browser.find_elements_by_xpath("//div[@class='app-checkbox']").eq(0).click() #получаем список элементов и кликаем в первый
        # browser.find_element_by_xpath("//label[@class='app-checkbox']").click() #OK

        element = browser.find_element_by_xpath("//*[contains(text(), 'liftarn_Black_horse.svg')]")
        parent = element.find_element_by_xpath('..')
        parent.find_element_by_xpath("./div[@class='files-editor-file__checkbox']//label[@class='app-checkbox']").click()
        