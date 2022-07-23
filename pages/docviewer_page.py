from .base_page import BasePage
from .locators import DocViewerPageLocators


class DocViewerPage(BasePage):
    text_origin = 'Хорошего тебе дня :)\n' \
                  'Вторая строка'

    def check_ER(self):
        """Проверяет текст"""
        text_current = ''
        text_file = self.driver.find_elements(*DocViewerPageLocators.TEXT_LIST)
        for string in text_file:
            text_string = string.text
            text_current += text_string + '\n'
        text_current = text_current[:-1]

        assert text_current == self.text_origin, 'Текст не соответствует ожиданиям.'

    def logout(self):
        """Выходит из аккаунта"""
        self.find_element(*DocViewerPageLocators.USER_PIC_DOCVIEWER).click()
        self.find_element(*DocViewerPageLocators.LOGOUT_BTN_DOCVIEWER).click()
