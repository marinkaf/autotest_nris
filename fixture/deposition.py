# -*- coding: utf-8 -*-

class DepositionHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        browser = self.app.browser
        elem_menu_deposition = browser.find_element_by_xpath("//span[contains(text(),'Депонирование')]")
        elem_menu_deposition.click()
        elem_submenu_deposition_AditAndPay = browser.find_element_by_xpath("//a[contains(text(),'Обработка и оплата (3)')]")        
        elem_submenu_deposition_AditAndPay.click()
        print("elem_submenu_deposition_AditAndPay.text =",elem_submenu_deposition_AditAndPay.get_attribute('innerHTML'))

    def loading_file(self, filepath):
        browser = self.app.browser

    def info_new(self):
        browser = self.app.browser

        #Ищем все элементы относящиеся к депонированным файлам 
        elements = browser.find_elements_by_xpath("//*[@class='cell-info__title']")
        
        def name_deposit(elem):
        # Вычленяем наименование депонированного файла
            name_deposit = list()
            for x in elem:
                attribute = x.get_attribute('innerHTML')
                attribute = attribute.replace(' ', '').replace('\n', '')
                name_deposit.append(attribute)
                # name_deposit[i] = i
            return(name_deposit)

                # print(elements)

        print("*************")
        print('name_deposit', name_deposit(elements))
        print("*************")