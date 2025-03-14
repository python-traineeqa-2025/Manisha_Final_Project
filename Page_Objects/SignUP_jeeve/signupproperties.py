from Page_Objects.SignUP_jeeve.signuplocators import Sign_Up_Locators

class Sign_Up_Properties(Sign_Up_Locators):

    @property
    def Myaccount_input(self):
        return self.driver.find_element(*Sign_Up_Locators.My_ACCOUNT)

    @property
    def login_button(self):
        return self.driver.find_element(*Sign_Up_Locators.LOGIN_BUTTON)
    @property
    def signup_button(self):
        return self.driver.find_element(*Sign_Up_Locators.SIGNUP_BUTTON)

    @property
    def mobile_input(self):
        return self.driver.find_element(*Sign_Up_Locators.MOBILE_NUM)

    @property
    def dob_input(self):
        return self.driver.find_element(*Sign_Up_Locators.DOB)

    @property
    def password_input(self):
        return self.driver.find_element(*Sign_Up_Locators.PASSWORD)

    @property
    def confirmpassword_input(self):
        return self.driver.find_element(*Sign_Up_Locators.CONFIRM_PASSWORD)

    @property
    def checkbox_input(self):
        return self.driver.find_element(*Sign_Up_Locators.CHECKBOX)

    @property
    def joinbtn_input(self):
        return self.driver.find_element(*Sign_Up_Locators.JOIN_BUTTON)
