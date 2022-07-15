from selenium.webdriver.common.by import By


class YandexMainPageLocators():
    AUTHORISATION_BTN = (By.CSS_SELECTOR, '[data-statlog="notifications.mail.logout.enter"]')
    DISK_BTN = (By.CSS_SELECTOR, '[data-statlog="notifications.mail.login.disk"]')


class LoginFormLocators():
    LOGIN_FIELD = (By.ID, 'passp-field-login')
    SIGN_IN_BTN = (By.ID, 'passp:sign-in')
    PASS_FIELD = (By.ID, 'passp-field-passwd')


class DiskPageLocators():
    FILE_FOR_COPY = (By.CSS_SELECTOR, '[aria-label="Файл для копирования.txt"]')
    CONTEXT_COPY = (By.CSS_SELECTOR, '[value="copy"]')
    CONTEXT_DELETE = (By.CSS_SELECTOR, '[value="delete"]')
    NEW_FOLDER_CONTEXT_COPY = (By.CSS_SELECTOR, '[title="Новая папка"]')
    COPY_BTN = (By.CLASS_NAME, 'confirmation-dialog__button_submit')
    NEW_FOLDER_MAIN = (By.CSS_SELECTOR, '[aria-label="Новая папка"]')
    FILES_LIST = (By.CSS_SELECTOR, '.listing__items [aria-label]')
    USER_PIC = (By.CSS_SELECTOR, '[aria-label="Аккаунт"]')
    LOGOUT_BTN = (By.CSS_SELECTOR, '[aria-label="Выйти из аккаунта"]')

