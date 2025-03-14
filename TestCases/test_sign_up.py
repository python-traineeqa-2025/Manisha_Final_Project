import logging
import time

from Page_Objects.SignUP_jeeve.signup import SignUp
from Setup.Basetest import BaseTest

class Testlog(BaseTest):

    def test_signup(self):

        url = self.creds["Base_url"]
        self.driver.get( url)
        logging.info("Opened the site")

        log_in = SignUp(self.driver)
        # logging.info("getting the credentials")

        log_in.signup()