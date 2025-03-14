
import logging
import time

from Setup.Basetest import BaseTest
from Page_Objects.CreateAccount_HealMeNepal.createpage import CreateAccount

class TestLogs(BaseTest):

    # def __init__(self, creds,driver):
    #     self.creds = creds
    #     self.driver = driver

    def test_create(self):
        url = self.creds["Base_url"]
        self.driver.get( url)
        logging.info("Opened the site")

        sign_up = CreateAccount(self.driver)

        fullname = self.creds["FullName"]
        email_ad = self.creds["Email"]
        pwd = self.creds["Password"]
        confirm_pwd = self.creds["Confirm Password"]

        logging.info("got the credentials ")

        sign_up.create(fullname,email_ad,pwd,confirm_pwd)

        logging.info("Account Created Successfully")


        time.sleep(10)