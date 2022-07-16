import time

from selenium.webdriver import ActionChains

from .base_page import BasePage
from .locators import DiskPageLocators


class DiskPage(BasePage):

    file_name_origin = 'Файл для копирования.txt'

    def copy(self):
        print('Копируем файл')
        action = ActionChains(self.driver)
        assert self.is_element_present(*DiskPageLocators.FILE_FOR_COPY), 'FILE_FOR_COPY not found'
        file_for_cope = self.driver.find_element(*DiskPageLocators.FILE_FOR_COPY)
        action.context_click(file_for_cope).perform()
        assert self.is_element_present(*DiskPageLocators.CONTEXT_COPY), 'CONTEXT_COPY not found'
        context_copy = self.driver.find_element(*DiskPageLocators.CONTEXT_COPY)
        context_copy.click()
        assert self.is_element_present(*DiskPageLocators.NEW_FOLDER_CONTEXT_COPY), 'NEW_FOLDER_CONTEXT_COPY not found'
        new_folder_context_copy = self.driver.find_element(*DiskPageLocators.NEW_FOLDER_CONTEXT_COPY)
        new_folder_context_copy.click()
        assert self.is_element_present(*DiskPageLocators.COPY_BTN), 'COPY_BTN not found'
        copy_btn = self.driver.find_element(*DiskPageLocators.COPY_BTN)
        copy_btn.click()
        time.sleep(3)

    def open_folder(self):
        print('Открываем папку')
        assert self.is_element_present(*DiskPageLocators.NEW_FOLDER_MAIN), 'NEW_FOLDER_MAIN not found'
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
        assert self.is_element_present(*DiskPageLocators.USER_PIC), 'USER_PIC not found'
        user_pic = self.driver.find_element(*DiskPageLocators.USER_PIC)
        user_pic.click()
        assert self.is_element_present(*DiskPageLocators.LOGOUT_BTN), 'LOGOUT_BTN not found'
        logout_btn = self.driver.find_element(*DiskPageLocators.LOGOUT_BTN)
        logout_btn.click()
        time.sleep(2)

    def check(self):
        files_list = self.driver.find_elements(*DiskPageLocators.FILES_LIST)
        assert len(files_list) == 1, 'В папке больше одного файла!'
        file_name = files_list[0].get_attribute("aria-label")
        assert file_name == self.file_name_origin, 'Название файла не соответствует оригиналу!'
        print('Скопированный файл находится в папке и его название соответствует оригиналу.')
