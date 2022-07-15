import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    url = 'https://www.yandex.ru/'
    print('\nStart Chrome browser for test...')
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # убирает ненужные системные логи варнинги (usb/ssl)
    driver = webdriver.Chrome(options=options)
    print('\nStart Yandex page')
    driver.get(url)
    driver.implicitly_wait(10)
    yield driver
    print('\nQuit browser')
    driver.quit()
