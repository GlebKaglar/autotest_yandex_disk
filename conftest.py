import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    url = 'https://www.ya.ru/'
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # убирает ненужные системные логи варнинги (usb/ssl)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
