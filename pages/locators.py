from selenium.webdriver.common.by import By


class YandexMainPageLocators():
    AUTHORISATION_BTN = (By.CSS_SELECTOR, '[data-statlog="headline.enter"]')
    AVATAR_BTN = (By.CLASS_NAME, 'avatar__image-wrapper')
    DISK_BTN = (By.CSS_SELECTOR, '[data-statlog="mail.login.usermenu.disk"]')


class LoginFormLocators():
    MAIL_BTN = (By.CSS_SELECTOR, '[data-type="login"]')
    LOGIN_FIELD = (By.ID, 'passp-field-login')
    SIGN_IN_BTN = (By.ID, 'passp:sign-in')
    PASS_FIELD = (By.ID, 'passp-field-passwd')


class DiskPageLocators():
    # Локаторы первого задания
    FILE_FOR_COPY = (By.CSS_SELECTOR, '[aria-label="Файл для копирования.txt"]')
    CONTEXT_COPY = (By.CSS_SELECTOR, '[value="copy"]')
    CONTEXT_DELETE = (By.CSS_SELECTOR, '[value="delete"]')
    NEW_FOLDER_CONTEXT_COPY = (By.CSS_SELECTOR, '[title="Новая папка"]')
    COPY_BTN = (By.CLASS_NAME, 'confirmation-dialog__button_submit')
    NEW_FOLDER_MAIN = (By.CSS_SELECTOR, '[aria-label="Новая папка"]')
    FILES_LIST = (By.CSS_SELECTOR, '.listing__items [aria-label]')
    USER_PIC = (By.CSS_SELECTOR, '[aria-label="Аккаунт"]')
    LOGOUT_BTN = (By.CSS_SELECTOR, '[aria-label="Выйти из аккаунта"]')

    # Локаторы задания со звездочкой
    CREATE_SMTH = (By.CSS_SELECTOR, '.LeftColumn__Buttons button')
    CREATE_FOLDER = (By.CSS_SELECTOR, '[aria-label="Папку"]')
    RENAME_FIELD = (By.CSS_SELECTOR, 'form > span > input')
    SAVE_BTN = (By.CSS_SELECTOR, '.confirmation-dialog__footer > button')
    FOLDER = (By.CSS_SELECTOR, '[aria-label="Папка для задания со звездочкой"]')
    UPLOAD_BTN = (By.CSS_SELECTOR, '[type="file"]')
    FILE = (By.CSS_SELECTOR, '.listing-item_theme_tile')


class DocViewerPageLocators():
    TEXT_LIST = (By.CSS_SELECTOR, 'div p')
    USER_PIC_DOCVIEWER = (By.CSS_SELECTOR, '.header__side-right > div')
    LOGOUT_BTN_DOCVIEWER = (By.CSS_SELECTOR, 'ul li:nth-child(2)')
