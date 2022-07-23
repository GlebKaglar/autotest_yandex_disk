import os

from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import DiskPageLocators


class DiskPage(BasePage):

    file_name_origin = 'Файл для копирования.txt'

    def copy(self):
        """Копирует файл в папку"""
        self.context_click(self.find_element(*DiskPageLocators.FILE_FOR_COPY))
        self.find_element(*DiskPageLocators.CONTEXT_COPY).click()
        self.find_element(*DiskPageLocators.NEW_FOLDER_CONTEXT_COPY).click()
        self.find_element(*DiskPageLocators.COPY_BTN).click()

    def open_folder_task_1(self):
        """Открывает папку"""
        self.double_click(self.find_element(*DiskPageLocators.NEW_FOLDER_MAIN))

    def delete_file(self, file):
        """Удаляет файл"""
        self.context_click(file)
        self.find_element(*DiskPageLocators.CONTEXT_DELETE).click()

    def delete_files(self):
        """Перебирает список на удаление"""
        files = self.driver.find_elements(*DiskPageLocators.FILES_LIST)
        for file in files:
            file_name = file.get_attribute("aria-label")
            if file_name != self.file_name_origin:
                self.delete_file(file)

    def logout(self):
        """Выходит из аккаунта"""
        self.find_element(*DiskPageLocators.USER_PIC).click()
        self.find_element(*DiskPageLocators.LOGOUT_BTN).click()

    def check_ER_1(self):
        """Проверяет с ОР_1: 'Скопированный файл находится в папке'"""
        files = self.driver.find_elements(*DiskPageLocators.FILES_LIST)
        assert len(files) == 1, 'В папке больше одного файла.'

    def check_ER_2(self):
        """Проверяет с ОР_2: 'Название соответствует оригиналу'"""
        files = self.driver.find_elements(*DiskPageLocators.FILES_LIST)
        file_name = files[0].get_attribute("aria-label")
        assert file_name == self.file_name_origin, 'Название файла не соответствует оригиналу.'

# Задача 2 (со звездочкой)
    def create_folder(self):
        """Создает новую папку"""
        self.find_element(*DiskPageLocators.CREATE_SMTH).click()
        self.find_element(*DiskPageLocators.CREATE_FOLDER).click()

        # В поле ввода вводим название папки, удалив перед этим текст плейсхолдера
        rename_field = self.find_element(*DiskPageLocators.RENAME_FIELD)
        rename_field.send_keys(Keys.CONTROL, 'a')
        rename_field.send_keys(Keys.BACK_SPACE)
        rename_field.send_keys('Папка для задания со звездочкой')

        self.find_element(*DiskPageLocators.SAVE_BTN).click()

    def open_folder_task_2(self):
        """Открывает папку"""
        self.double_click(self.find_element(*DiskPageLocators.FOLDER))

    def upload_file(self):
        """Загружает файл"""
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'Файл для задания со звездочкой.txt')
        self.find_element(*DiskPageLocators.UPLOAD_BTN).send_keys(file_path)

    def open_file(self):
        """Открывает файл и переходит на вкладку, где открылся файл"""
        self.double_click(self.find_element(*DiskPageLocators.FILE))
        self.driver.switch_to.window(self.driver.window_handles[2])
