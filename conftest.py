import pytest

from model.registration import Registration_data
from fixture.application import Application
from fixture.deposition import DepositionHelper

fixture = None

@pytest.fixture(scope="session", autouse=True)
def app(request):
#Эта fixture будет выполняться перед каждым тестом
    global fixture
    if fixture is None:
        fixture = Application() #Инициализация fixture
        '''
        #так можно добавить авторизацию в fixture, тогда понадобится удалить из всех тестов авторизацию
        fixture.session.logaut(username = "bus1-fl@mail.ru", password = "Qwerty12")
        '''
    else:
        if not fixture.is_valid():
            fixture = Application() #Инициализация fixture
            '''
            #так можно добавить авторизацию в fixture, тогда понадобится удалить из всех тестов авторизацию
            fixture.session.logaut(username = "bus1-fl@mail.ru", password = "Qwerty12")
            '''
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    request.addfinalizer(fixture.destroy) #Разрушаем fixture
    