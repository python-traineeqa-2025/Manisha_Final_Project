import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_Objects.CreateAccount_HealMeNepal.createpageproperties import Create_Page_Properties

class CreateAccount(Create_Page_Properties):

    def __init__(self,driver):
        self.driver = driver


    def create(self,name,email,password,confirm_pwd):

        login_btn = self.login_btn_input
        login_btn.click()
        time.sleep(1)

        create_account = self.signin_btn_input
        create_account.click()
        time.sleep(1)

        fullname = self.fullname_input
        fullname.send_keys(name)
        time.sleep(1)

        Email = self.email_input
        Email.send_keys(email)
        time.sleep(2)

        Password = self.password_input
        Password.send_keys(password)
        time.sleep(1)

        Confirm_Password = self.confirm_pwd_input
        Confirm_Password.send_keys(confirm_pwd)
        time.sleep(1)

        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
        )
        self.driver.switch_to.frame(iframe)

        # Locate and click the checkbox
        checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id="recaptcha-anchor-label"]'))
        )
        checkbox.click()

        # Switch back to the default content
        self.driver.switch_to.default_content()

        time.sleep(1)

        create = self.create_btn
        create.click()
        time.sleep(2)
















