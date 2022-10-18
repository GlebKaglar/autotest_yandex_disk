from .utils.authorization import authorization
from ..pages.disk_page import DiskPage
from ..pages.docviewer_page import DocViewerPage


def test_upload_file_to_new_folder(driver):
    """
    Проверяет загрузку текстового файла, затем проверяет его текст.
    ОР: Текст соответствует ожиданиям
    """
    authorization(driver)

    disk_page = DiskPage(driver)
    disk_page.create_folder()
    disk_page.open_folder_task_2()
    disk_page.upload_file()
    disk_page.open_file()

    docviewer_page = DocViewerPage(driver)
    docviewer_page.check_ER()
    docviewer_page.logout()