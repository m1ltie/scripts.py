from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


class Test:
    def test(self):
        options = ChromeOptions()
        driver = Chrome(options=options)
        driver.get('https://skillbox.ru')
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title
