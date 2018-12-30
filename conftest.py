import pytest

from model.registration import Registration_data
from fixture.application import Application
from fixture.deposition import DepositionHelper



@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture