from ..pages.base_page import BasePage
from ..pages.disk_page import DiskPage
from ..pages.docviewer_page import DocViewerPage


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
