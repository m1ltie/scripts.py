import pytest
from selenium.webdriver.chrome import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver

class test1:
    def test_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox - образовательная платформа с онлайн-курсами' == driver.title
