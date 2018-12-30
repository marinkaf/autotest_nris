import time

# OK 
def test_loginOK(app):
    app.open_page(url='http://devel.nris.ru/')
    time.sleep(5)
    app.session.logaut(username = "bus1@gmail.com", password = "Qwerty12")
    time.sleep(5)
    # app.session.wait()
    # time.sleep(5)
    # app.session.openPersonalKabinet()
    # time.sleep(5)

# # OK  
# def test_loginFail(app):
#     app.open_page()
#     time.sleep(5)
#     app.logaut(username = "marinalyamina@yandex.ru", password = "Qwerty12")
#     # app.session.wait()
#     assert True

def test_newPPA(app):
    app.session.openPersonalKabinet()
    app.session.registrationPPA()
    time.sleep(15)