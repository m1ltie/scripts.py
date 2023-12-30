import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture
def set_up_browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class test1:
    def test_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox - образовательная платформа с онлайн-курсами' == driver.title
