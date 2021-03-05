from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FIELD = (By.XPATH, '//input[@id="input-username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="input-password"]')
    ERROR_ALERT = (By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[text()="Forgotten Password"]')
    ENTER_BUTTON = (By.XPATH, '//button[@type="submit"]')


class AdminPageLocators():
    CATALOG_BUTTON = (By.XPATH, '//a[@href="#collapse1"]')
    PRODUCT_BUTTON = (By.XPATH, '//ul[@id="collapse1"]/li[2]')
    DOWNLOAD_BUTTON = (By.XPATH, '//ul[@id="collapse1"]/li[8]')
    ADD_NEW_BUTTON = (By.XPATH, '//a[@data-original-title="Add New"]')
    DELETE_BUTTON = (By.XPATH, '//button[@class="btn btn-danger"]')
    NEW_PRODUCT_CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    PERMISSION_ALERT = (By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]')
    EDIT_BUTTONS = (By.XPATH, '//a[@data-original-title="Edit"]')


class ProductAddAndEditPageLocators():
    PRODUCT_NAME_FIELD = (By.XPATH, '//*[@id="input-name1"]')
    META_TAG_FIELD = (By.XPATH, '//*[@id="input-meta-title1"]')
    DESCRIPTION_FIELD = (By.XPATH, '//div[@class="note-editable panel-body"]')
    META_TAG_DESCRIPTION_FIELD = (By.XPATH, '//*[@id="input-meta-description1"]')
    META_TAG_KEYWORDS_FIELD = (By.XPATH, '//*[@id="input-meta-keyword1"]')
    PRODUCT_TAGS_FIELD = (By.XPATH, '//*[@id="input-tag1"]')

    DATA_PAGE = (By.XPATH, '//a[@href="#tab-data"]')
    MODEL_FIELD = (By.XPATH, '//*[@id="input-model"]')
    LINKS_PAGE = (By.XPATH, '//a[@href="#tab-links"]')
    CATEGORIES_FIELD = (By.XPATH, '//*[@id="input-category"]')
    MONITOR_CATEGORIES_SELECT = (By.XPATH, '//li[@data-value="28"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SUCCESS_ALERT = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')

    ATTRIBUTE_PAGE = (By.XPATH, '//a[@href="#tab-attribute"]')
    REMOVE_1_BUTTON = (By.XPATH, '//button[@onclick="$(\'#attribute-row0\').remove();"]')
    REMOVE_2_BUTTON = (By.XPATH, '//button[@onclick="$(\'#attribute-row1\').remove();"]')
    OPTION_PAGE = (By.XPATH, '//a[@href="#tab-option"]')
    INPUT_OPTION = (By.XPATH, '//input[@id="input-option"]')
    DELIVERY_DATE = (By.XPATH, '//li[@data-value="12"]')
    REQUIRED_SELECT = (By.XPATH, '//select[@id="input-required0"]')
    NO_SELECT = (By.XPATH, '//select[@id="input-required0"]/*[@value="0"]')


class DownloadPageLocators():
    UPLOAD_BUTTON = (By.XPATH, '//button[@id="button-upload"]')
    FILENAME_FIELD_JS = (By.XPATH, '//input[@type="file"]')



