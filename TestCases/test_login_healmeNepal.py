import logging
import time

from Page_Objects.Login.login import Login
from Setup.Basetest import BaseTest


class Testlog(BaseTest):

    def test_login(self):
        url = self.creds["Base_url"]
        self.driver.get(url)
        logging.info("Opened the site")

        log_in = Login(self.driver)

        email_id = self.creds["Email"]
        pwd = self.creds["Password"]

        logging.info("got the credentials now logging in")

        log_in.login(email_id,pwd)
        time.sleep(10)
        logging.info("Logged In Successfully")

        time.sleep(10)
