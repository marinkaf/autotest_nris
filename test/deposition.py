from model.registration import Registration_data
from fixture.application import Application, DepositionHelper

import time

def test_deposit(app):
    app.open_page(url='http://devel.nris.ru/')
    time.sleep(5)
    app.session.logaut(username = "bus1@gmail.com", password = "Qwerty12")
    time.sleep(5)
    app.deposition.open()
    app.deposition.info_new()

