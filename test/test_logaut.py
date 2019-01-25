import time
from model.registration import Registration_data
from model.registration import Person_fl_data

# OK 
def test_login(app):
    app.open_page(url='http://devel.nris.ru/')
    time.sleep(5)
    # app.session.logaut(Registration_data(username = "bus1@gmail.com", password = "Qwerty12"))
    app.session.logaut(Registration_data(username = "bus1-fl@mail.ru", password = "Qwerty12"))
    time.sleep(5)
    # app.session.wait()
    # time.sleep(5)
    # app.session.openProfileMenu()
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
    # app.session.clickOnLogo()
    app.session.openProfileMenu()
    app.session.openPersonalKabinet()
    app.session.registrationPPA()
    time.sleep(15)


def test_EditProfileFl(app):
    # app.session.clickOnLogo()
    app.session.clickOnLogo()
    app.session.openProfileMenu()
    app.session.openProfile()
    app.session.editProfile(Person_fl_data(surname = "Surname_2", phone_number = "898989898"))    