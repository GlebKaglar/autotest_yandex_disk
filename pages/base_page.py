import time

from selenium.common import NoSuchElementException

from .locators import YandexMainPageLocators, LoginFormLocators


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def login(self):
        print('Авторизация')
        login = 'glebtestodin'
        password = '_GlebTest1'

        assert self.is_element_present(*YandexMainPageLocators.AUTHORISATION_BTN), 'AUTHORISATION_BTN not found'
        print('Нажимаем Войти на главной странице Яндекса')
        authorisation_btn = self.driver.find_element(*YandexMainPageLocators.AUTHORISATION_BTN)
        authorisation_btn.click()

        assert self.is_element_present(*LoginFormLocators.MAIL_BTN), 'MAIL_BTN not found'
        print('Выбираем способ входа через почту')
        mail_btn = self.driver.find_element(*LoginFormLocators.MAIL_BTN)
        mail_btn.click()

        assert self.is_element_present(*LoginFormLocators.LOGIN_FIELD), 'LOGIN_FIELD not found'
        print('Вводим логин')
        login_field = self.driver.find_element(*LoginFormLocators.LOGIN_FIELD)
        login_field.send_keys(login)

        assert self.is_element_present(*LoginFormLocators.SIGN_IN_BTN), 'SIGN_IN_BTN not found'
        print('Нажимаем Войти в форме авторизации')
        sign_in_btn = self.driver.find_element(*LoginFormLocators.SIGN_IN_BTN)
        sign_in_btn.click()

        assert self.is_element_present(*LoginFormLocators.PASS_FIELD), 'PASS_FIELD not found'
        print('Вводим пароль')
        pass_field = self.driver.find_element(*LoginFormLocators.PASS_FIELD)
        pass_field.send_keys(password)

        assert self.is_element_present(*LoginFormLocators.SIGN_IN_BTN), 'SIGN_IN_BTN not found'
        print('Нажимаем Войти после ввода пароля')
        sign_in_btn = self.driver.find_element(*LoginFormLocators.SIGN_IN_BTN)
        sign_in_btn.click()

        time.sleep(5)

    def go_to_disk(self):
        assert self.is_element_present(*YandexMainPageLocators.DISK_BTN), 'DISK_BTN not found'
        print('Открываем Диск')
        disk_btn = self.driver.find_element(*YandexMainPageLocators.DISK_BTN)
        disk_btn.click()

        print('Переходим на взаимодействие со вкладкой, где открылся Диск')
        window_disk = self.driver.window_handles[1]
        self.driver.switch_to.window(window_disk)
        time.sleep(5)


