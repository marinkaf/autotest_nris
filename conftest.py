import pytest

from model.registration import Registration_data
from fixture.application import Application
from fixture.deposition import DepositionHelper



@pytest.fixture(scope = "session")
def app(request):
#Эта fixture будет выполняться перед каждым тестом
    fixture = Application() #Инициализация fixture
    request.addfinalizer(fixture.destroy) #Разрушаем fixture
    return fixture