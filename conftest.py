
import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")  # (scope = "session") => позволяет выполнять все тесты в одной сессии браузера
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

