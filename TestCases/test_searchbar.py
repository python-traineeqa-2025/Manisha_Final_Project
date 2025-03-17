import logging

from Page_Objects.SearchBar.SearchBar import SearchBar
from Setup.Basetest import BaseTest


class TestSearch(BaseTest):


    def test_search(self):

        url = self.creds["Base_url"]
        self.driver.get(url)
        logging.info("Opened the site")

        search = SearchBar(self.driver)

        search.valid_input_searchbar()
        logging.info("Search for the required product passed: List of products were displayed")
        search.empty_searchbar()

        search.invalid_input()

        logging.info("Empty search test passed: Home page is refreshed")

        search.test_auto_suggestions()






