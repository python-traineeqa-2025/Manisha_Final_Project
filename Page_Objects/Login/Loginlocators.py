from selenium.webdriver.common.by import By

class Login_Locators(object):

    LOGIN_BTN =(By.XPATH,'//a[@title=\'Log In\']')
    EMAIL = (By.ID,'email')
    PASSWORD = (By.ID,'password')
    CHECK_BOX = (By.ID, 'recaptcha-anchor-label')
    LOGIN = (By.XPATH,'//button[normalize-space()=\'Login\']')