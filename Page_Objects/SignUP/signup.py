# from webdriver_manager.core import driver
from selenium.webdriver.support.wait import WebDriverWait

from Page_Objects.SignUP.signupproperties import Sign_Up_Properties

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC




class SignUp(Sign_Up_Properties):

    def __init__(self,driver):
        self.driver = driver

    def signup(self):
        my_account = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.My_ACCOUNT))

        login_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(my_account).move_to_element(login_btn).click().perform()