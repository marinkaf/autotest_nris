# -*- coding: utf-8 -*-

import time

class SessinHelper:

    def __init__(self, app):
        self.app = app

    def logaut(self, Registration_data):
        browser = self.app.browser
        elem_login = browser.find_element_by_link_text('Войти')
        elem_login.click()
        # wait = WebDriverWait(browser, 20)
        elem_email = browser.find_element_by_id("email")
        elem_email.clear()
        elem_email.send_keys(Registration_data.username)      
        elem_password = browser.find_element_by_id("password")
        elem_password.clear()
        elem_password.send_keys(Registration_data.password)
        elem_button_submit = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]")
        elem_button_submit.click()
        #try:
        #    elem_profile_menu = browser.find_element_by_xpath("//div[@class='profile-menu__username']")
     
    def wait(self):
        browser = self.app.browser
        browser.find_element_by_xpath("//a[@class='header__user-link']").click()
        
        element = browser.find_element_by_xpath("//*[contains(text(), 'Выйти')]")
        parent = element.find_element_by_xpath('..')
        parent.click()
        # browser.find_element_by_xpath("//*[text()='Выйти']").click()

    def openProfileMenu(self):
        browser = self.app.browser
        browser.find_element_by_xpath("//a[@class='header__user-link']").click()

    def openPersonalKabinet(self):
        browser = self.app.browser
        element = browser.find_element_by_xpath("//*[contains(text(), 'Личный кабинет')]")
        parent = element.find_element_by_xpath('..')
        parent.click()    

    def openProfile(self):
        browser = self.app.browser
        element = browser.find_element_by_xpath("//*[contains(text(), 'Редактировать аккаунт')]")
        parent = element.find_element_by_xpath('..')
        parent.click()

    def registration(self, Registration_data):
        browser = self.app.browser
        elem_email = browser.find_element_by_id('email')
        elem_email.clear()
        elem_email.send_keys(Registration_data.username)
        elem_password = browser.find_element_by_id('password')
        elem_password.clear()
        elem_password.send_keys(Registration_data.password)
        elem_password_confirm = browser.find_element_by_id('password-confirm')
        elem_password_confirm.clear()
        elem_password_confirm.send_keys(Registration_data.password)
        elem_code = browser.find_element_by_id('code')
        elem_code.clear()
        elem_code.send_keys(Registration_data.code)
        checkbox_1 = browser.find_element_by_xpath("//div[@class='register-form__license form__field form__field--checkbox form-field form-field--checkbox checkbox-field']//span[@class='checkbox-field__check']")
        checkbox_1.click()
        checkbox_2 = browser.find_element_by_xpath("//div[@class='register-form__personal form__field form__field--checkbox form-field form-field--checkbox checkbox-field']//span[@class='checkbox-field__check']")
        checkbox_2.click()
        button_submit = browser.find_element_by_xpath("//button[@type='submit']")
        button_submit.click()
        browser.find_element_by_xpath("//h1[contains(text(),'Ваши данные проверяются модератором')]")



    def registrationPPA(self):
        browser = self.app.browser
        browser.find_element_by_xpath("//*[contains(text(), 'Новый аккаунт')]/..").click()
        time.sleep(2)
        browser.find_element_by_xpath("//input[@placeholder='Выбрать']").click()
        browser.find_element_by_xpath("//*[contains(text(), 'Физическое лицо')]").click()
        time.sleep(2)
        browser.find_element_by_xpath("//label[contains(text(),'Email')]/../input").send_keys('busfl11@mail.ru')
        # тоже самое другим xpath
        # browser.find_element_by_xpath("//div[@class='app-form']//div[4]//div[1]//div[1]//div[1]//input[1]").send_keys('busfl11@mail.ru')
        browser.find_element_by_name("phone").send_keys('9612618330')
        browser.find_element_by_xpath("//label[contains(text(),'Фамилия')]/../input").send_keys('ФамилияППАФЛ')
        browser.find_element_by_xpath("//label[contains(text(),'Имя')]/../input").send_keys('ИмяППАФЛ')
        browser.find_element_by_xpath("//label[contains(text(),'Отчество')]/../input").send_keys('ОтчествоППАФЛ')
        elemdata = browser.find_element_by_xpath("//label[contains(text(),'Дата рождения')]/../..").click()
        


        browser.find_element_by_xpath("//label[contains(text(),'Серия и № паспорта')]/../input").send_keys('1111 525852')
        browser.find_element_by_xpath("//label[contains(text(),'Когда выдан паспорт')]/../input").send_keys('01-01-2000')
        browser.find_element_by_xpath("//label[contains(text(),'Кем выдан паспорт')]/../input").send_keys('УФМС')
        browser.find_element_by_xpath("//label[contains(text(),'Код подразделения')]/../input").send_keys('052135')
        browser.find_element_by_xpath("//label[contains(text(),'Адрес регистрации')]/../input").send_keys('Адрес регистрации введен вручную')

        browser.find_element_by_xpath("//div[@class='app-form']//div[17]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]").sendFile("/home/marinka/Загрузки")
        browser.find_element_by_xpath("//div[@class='app-form']//div[18]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]").sendFile("/home/marinka/Загрузки")


    def editProfile(self, Person_fl_data):
        browser = self.app.browser
        if Person_fl_data.phone_number is not None: #эта конструкция нужна, если мы хотим использовать функцию не для заполнения пустого профиля при регистрации, а для изменения данных у существующего
            elem_phone_number = browser.find_elements_by_id('phone')
            elem_phone_number.clear()
            elem_phone_number.send_keys(Person_fl_data.phone_number)
        if Person_fl_data.surname is not None:
            elem_input_surname = browser.find_element_by_name('surname')
            elem_input_surname.clear()
            elem_input_surname.send_keys(Person_fl_data.surname)
        #Ищем кнопку "Сохранить"
        browser.find_element_by_xpath("//button[@type='submit']").click()
        #Проверяем что форма отправлена на модерацию
        browser.find_element_by_xpath("//h1[contains(text(),'Ваши данные проверяются модератором')]")

    def clickOnLogo(self):
        browser = self.app.browser
        browser.find_element_by_class_name("profile-menu-wrapper profile-menu-wrapper--hidden").click()