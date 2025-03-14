from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Login.LoginProperties import Login_Properties

class Login(Login_Properties):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email_id, pwd):
        login_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='Log In']"))
        )
        login_link.click()

        email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys(email_id)

        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.send_keys(pwd)

        # Handle CAPTCHA if present
        try:
            iframe = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
            )
            self.driver.switch_to.frame(iframe)

            checkbox = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[id="recaptcha-anchor-label"]'))
            )
            checkbox.click()

            self.driver.switch_to.default_content()
        except:
            pass  # CAPTCHA not present

        login_btn = self.login_button
        login_btn.click()

        # # Verify successful login
        # WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.ID, "user_profile"))
        # )