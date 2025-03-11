import logging
import time

from Setup.Basetest import BaseTest

class Testlog(BaseTest):

    def test_url(self):

        url = self.creds['Base_url']
        self.driver.get(url)
        time.sleep(5)

        logging.info("OLIZ STORE.COM")
        title = self.driver.title
        logging.info("SITE OPENED:")