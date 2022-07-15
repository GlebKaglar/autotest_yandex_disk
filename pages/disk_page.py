import time

from selenium.webdriver import ActionChains

from .base_page import BasePage
from .locators import DiskPageLocators


class DiskPage(BasePage):

    file_name_origin = 'Файл для копирования.txt'

    def copy(self):
        print('Копируем файл')
        action = ActionChains(self.driver)
        file_for_cope = self.driver.find_element(*DiskPageLocators.FILE_FOR_COPY)
        action.context_click(file_for_cope).perform()
        context_copy = self.driver.find_element(*DiskPageLocators.CONTEXT_COPY)
        context_copy.click()
        new_folder_context_copy = self.driver.find_element(*DiskPageLocators.NEW_FOLDER_CONTEXT_COPY)
        new_folder_context_copy.click()
        copy_btn = self.driver.find_element(*DiskPageLocators.COPY_BTN)
        copy_btn.click()
        time.sleep(3)

    def open_folder(self):
        print('Открываем папку')
        new_folder_main = self.driver.find_element(*DiskPageLocators.NEW_FOLDER_MAIN)
        action = ActionChains(self.driver)
        action.double_click(new_folder_main).perform()

    def delete_file(self, file):
        print('Удаление файла')
        action = ActionChains(self.driver)
        action.context_click(file).perform()
        context_delete = self.driver.find_element(*DiskPageLocators.CONTEXT_DELETE)
        context_delete.click()

    def delete_files(self):
        files_list = self.driver.find_elements(*DiskPageLocators.FILES_LIST)
        for file in files_list:
            file_name = file.get_attribute("aria-label")
            if file_name != self.file_name_origin:
                self.delete_file(file)
        time.sleep(2)

    def logout(self):
        user_pic = self.driver.find_element(*DiskPageLocators.USER_PIC)
        user_pic.click()
        logout_btn = self.driver.find_element(*DiskPageLocators.LOGOUT_BTN)
        logout_btn.click()
        time.sleep(2)

    def check(self):
        files_list = self.driver.find_elements(*DiskPageLocators.FILES_LIST)
        assert len(files_list) == 1, 'В папке больше одного файла!'
        file_name = files_list[0].get_attribute("aria-label")
        assert file_name == self.file_name_origin, 'Название файла не соответствует оригиналу!'
        print('Скопированный файл находится в папке и его название соответствует оригиналу.')
