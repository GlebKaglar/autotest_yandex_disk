from environments.selenium_env.autotest_yandex_disk.pages.base_page import BasePage
from environments.selenium_env.autotest_yandex_disk.pages.disk_page import DiskPage


def test_copied_file(driver):
    print('Запуск теста')
    base_page = BasePage(driver)
    base_page.login()
    base_page.go_to_disk()

    disk_page = DiskPage(driver)
    disk_page.copy()
    disk_page.open_folder()
    disk_page.delete_files()
    disk_page.check()
    disk_page.logout()
