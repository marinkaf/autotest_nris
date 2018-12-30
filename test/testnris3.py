# -*- coding: utf-8 -*-

import time

from model.registration import Registration_data
from fixture.application import Application



#TESTS

# OK
def test_prifile(app):
    app.open_page(url='http://devel.nris.ru/')
    app.session.logaut(username = "marinalyamina89@yandex.ru", password = "Qwerty12")
    app.cookies()
    app.profile_menu()
    time.sleep(1)
        
# # OK нужно переделать axcept
# def test_registration(app):
#     app.open_page()
#     time.sleep(1)
#     try: 
#         app.session.registration(Registration_data(username = "test_check_in@mail.ru", password = "Qwerty12", code = ""))
#     except: # take a screenshot of failed
#         app.browser.save_screenshot("Регистрация_не_завершена.png")
#         assert False

# OK
# def test_catalog(app):
#     app.open_page()
#     time.sleep(1)
#     app.session.logaut(username = "marinalyamina89@yandex.ru", password = "Qwerty12")
#     time.sleep(0)
#     app.katalog.open()
#     time.sleep(3)
#     app.katalog.find_file_AditAndPay()
#     time.sleep(5)

