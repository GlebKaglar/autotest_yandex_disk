from ..pages.base_page import BasePage
from ..pages.disk_page import DiskPage


def test_copied_file(driver):
    print('Запуск теста')
    base_page = BasePage(driver)
    base_page.login()
    base_page.go_to_disk()

    disk_page = DiskPage(driver)
    disk_page.copy()
    disk_page.open_folder_task_1()
    disk_page.delete_files()
    disk_page.check_task_1()
    disk_page.logout()
