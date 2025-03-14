from Page_Objects.CreateAccount_HealMeNepal.createpagelocators import Create_Page_Locators

class Create_Page_Properties(Create_Page_Locators):

    @property
    def login_btn_input(self):
        return self.driver.find_element(*Create_Page_Locators.LOGIN_BTN)

    @property
    def signin_btn_input(self):
        return self.driver.find_element(*Create_Page_Locators.CREATE_ACCOUNT)

    @property
    def fullname_input(self):
        return self.driver.find_element(*Create_Page_Locators.FULLNAME)

    @property
    def email_input(self):
        return self.driver.find_element(*Create_Page_Locators.EMAIL_ADDRESS)

    @property
    def password_input(self):
        return self.driver.find_element(*Create_Page_Locators.PASSWORD)

    @property
    def confirm_pwd_input(self):
        return self.driver.find_element(*Create_Page_Locators.CONFORM_PASSWORD)

    @property
    def checkbox_input(self):
        return  self.driver.find_element(*Create_Page_Locators.CHECK_BOX)

    @property
    def create_btn(self):
        return self.driver.find_element(*Create_Page_Locators.CREATE)