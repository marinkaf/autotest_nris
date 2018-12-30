# -*- coding: utf-8 -*-

class DepositionHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        browser = self.app.browser
        elem_menu_deposition = browser.find_element_by_xpath("//span[contains(text(),'Депонирование')]")
        elem_menu_deposition.click()
        elem_submenu_deposition_AditAndPay = browser.find_element_by_xpath("//a[contains(text(),'Обработка и оплата (6)')]")        
        elem_submenu_deposition_AditAndPay.click()

    def loading_file(self, filepath):
        browser = self.app.browser