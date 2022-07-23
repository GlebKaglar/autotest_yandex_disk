from ...pages.base_page import BasePage


def authorization(driver):
    base_page = BasePage(driver)
    base_page.login()
    base_page.go_to_disk()
