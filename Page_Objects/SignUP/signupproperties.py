from Page_Objects.SignUP.signuplocators import Sign_Up_Locators

class Sign_Up_Properties(Sign_Up_Locators):

    @property
    def Myaccount_input(self):
        return self.driver.find_element(*Sign_Up_Locators.My_ACCOUNT)

    def login_button(self):
        return self.driver.find_element(*Sign_Up_Locators.LOGIN_BUTTON)