from .utils.authorization import authorization
from ..pages.disk_page import DiskPage


def test_copy_file_to_previously_created_folder(driver):
    """
    Проверяет копирование файла в созданную раннее папку, с последующим удалением всех  файлов в этой папке,
    кроме скопированного файла.

    ОР_1: Скопированный файл находится в папке
    ОР_2: Название соответствует оригиналу
    """
    authorization(driver)

    disk_page = DiskPage(driver)
    disk_page.copy()
    disk_page.open_folder_task_1()
    disk_page.delete_files()
    disk_page.check_ER_1()
    disk_page.check_ER_2()
    disk_page.logout()
