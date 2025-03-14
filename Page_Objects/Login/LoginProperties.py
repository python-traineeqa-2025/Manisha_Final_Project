from Page_Objects.Login.Loginlocators import Login_Locators

class Login_Properties(Login_Locators):

    @property
    def login_link_input(self):
        return self.driver.find_element(*Login_Locators.LOGIN_BTN)

    @property
    def emailid_input(self):
        return self.driver.find_element(*Login_Locators.EMAIL)

    @property
    def pwd_input(self):
        return self.driver.find_element(*Login_Locators.PASSWORD)

    @property
    def login_button(self):
        return self.driver.find_element(*Login_Locators.LOGIN_BTN)