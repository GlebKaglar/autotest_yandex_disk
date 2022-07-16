from environments.selenium_env.autotest_yandex_disk.pages.base_page import BasePage
from environments.selenium_env.autotest_yandex_disk.pages.disk_page import DiskPage
from environments.selenium_env.autotest_yandex_disk.pages.docviewer_page import DocViewerPage


def test_copied_file(driver):
    print('Запуск теста')
    base_page = BasePage(driver)
    base_page.login()
    base_page.go_to_disk()

    disk_page = DiskPage(driver)
    disk_page.create_folder()
    disk_page.open_folder_task_2()
    disk_page.upload_file()
    disk_page.open_file()

    docviewer_page = DocViewerPage(driver)
    docviewer_page.check_text()
    docviewer_page.logout()
