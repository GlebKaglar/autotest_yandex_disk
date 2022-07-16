import time

from .base_page import BasePage
from .locators import DocViewerPageLocators


class DocViewerPage(BasePage):
    text_origin = 'Хорошего тебе дня :)\n' \
                  'Вторая строка'

    def check_text(self):
        print('Проверяем текст')
        text_current = ''
        text_file = self.driver.find_elements(*DocViewerPageLocators.TEXT_LIST)
        for string in text_file:
            text_string = string.text
            text_current += text_string + '\n'
        text_current = text_current[:-1]

        assert text_current == self.text_origin, 'Текст не соответствует ожиданиям!'
        time.sleep(2)

    def logout(self):
        print('Выходим из аккаунта')
        assert self.is_element_present(*DocViewerPageLocators.USER_PIC_DOCVIEWER), 'USER_PIC_DOCVIEWER not found'
        user_pic = self.driver.find_element(*DocViewerPageLocators.USER_PIC_DOCVIEWER)
        user_pic.click()
        assert self.is_element_present(*DocViewerPageLocators.LOGOUT_BTN_DOCVIEWER), 'LOGOUT_BTN_DOCVIEWER not found'
        logout_btn = self.driver.find_element(*DocViewerPageLocators.LOGOUT_BTN_DOCVIEWER)
        logout_btn.click()
        time.sleep(2)
