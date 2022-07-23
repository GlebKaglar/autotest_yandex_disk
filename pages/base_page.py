from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import YandexMainPageLocators, LoginFormLocators


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def find_element(self, how, what):
        return WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((how, what))
        )

    def login(self):
        """Авторизовывается"""
        login = 'glebtestodin'
        password = '_GlebTest1'

        self.find_element(*YandexMainPageLocators.AUTHORISATION_BTN).click()
        self.find_element(*LoginFormLocators.MAIL_BTN).click()
        self.find_element(*LoginFormLocators.LOGIN_FIELD).send_keys(login)
        self.find_element(*LoginFormLocators.SIGN_IN_BTN).click()
        self.find_element(*LoginFormLocators.PASS_FIELD).send_keys(password)
        self.find_element(*LoginFormLocators.SIGN_IN_BTN).click()  # Еще раз получаем кнопку, т.к. обновился DOM

    def go_to_disk(self):
        """Открывает Диск и переходит на вкладку, где открылся Диск"""
        self.find_element(*YandexMainPageLocators.DISK_BTN).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def context_click(self, smth):
        """Клик ПКМ"""
        self.action.context_click(smth).perform()

    def double_click(self, smth):
        """Двойной клик"""
        self.action.double_click(smth).perform()
