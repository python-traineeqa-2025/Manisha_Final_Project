from selenium.webdriver.common.by import By


class Sign_Up_Locators(object):
    My_ACCOUNT = (By.XPATH,'//*[@id="__next"]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[1]')
    LOGIN_BUTTON = (By.XPATH,'//*[@id="__next"]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div[9]')
    SIGNUP_BUTTON = (By.XPATH,'//div[@class=\'text-primary-500 inline ml-1 cursor-pointer\']')
    MOBILE_NUM = (By.XPATH,'//input[@placeholder=\'Mobile Number *\']')
    DOB = (By.XPATH,'//div[contains(@class,\'flex flex-col items-center\')]//input[contains(@placeholder,\'Date of Birth *:\')]')
    PASSWORD = (By.XPATH,'//form[contains(@class,\'w-full\')]//div[1]//div[1]//input[1]')
    CONFIRM_PASSWORD = (By.XPATH,'//input[@placeholder=\'Confirm Password *\']')
    CHECKBOX = (By.XPATH,'//input[@id=\'Agree terms\']')
    JOIN_BUTTON = (By.XPATH,'//button[contains(@class,\'mt-6\')]')


