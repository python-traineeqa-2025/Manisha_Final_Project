from selenium.webdriver.common.by import By
class Create_Page_Locators(object):

    LOGIN_BTN = (By.XPATH,'//a[@title=\'Log In\']')
    CREATE_ACCOUNT = (By.XPATH,'//a[normalize-space()=\'Create your account\']')
    FULLNAME = (By.ID,'name')
    EMAIL_ADDRESS = (By.ID, "email")
    PASSWORD = (By.ID,'password')
    CONFORM_PASSWORD = (By.ID,'password_confirmation')
    CHECK_BOX = (By.ID,'recaptcha-anchor-label')
    CREATE = (By.XPATH,'//button[normalize-space()=\'Create\']')

