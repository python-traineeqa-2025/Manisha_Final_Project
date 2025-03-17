import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Page_Objects.SearchBar.searchbarproperties import Search_Bar_Properties
from selenium.webdriver.support import expected_conditions as EC

class SearchBar(Search_Bar_Properties):

    def __init__(self, driver):
        self.driver = driver


    def valid_input_searchbar(self):

        search_icon = self.search_icon_input
        search_icon.click()
        time.sleep(2)

        search_input = self.serach_bar_inputfield
        search_input.send_keys("Sunscreen")
        time.sleep(2)

        search_btn = self.search_button
        search_btn.click()
        time.sleep(5)

        # Auto_suggestion = self.autosuggestion
        # Auto_suggestion.click()


    def empty_searchbar(self):

        search_icon = self.search_icon_input
        search_icon.click()
        time.sleep(2)

        search_field = self.serach_bar_inputfield
        search_field.clear()
        time.sleep(3)

        search_btn = self.search_button
        search_btn.click()
        time.sleep(5)

        homepage_element = self.home_page_element
        homepage_element.is_displayed()

    def invalid_input(self):
        search_icon = self.search_icon_input
        search_icon.click()
        time.sleep(2)

        search_input = self.serach_bar_inputfield
        search_input.send_keys("hjdashdgahs")
        time.sleep(2)

        search_btn = self.search_button
        search_btn.click()
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        invalid_search_message = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Search results for hjdashdgahs']")))

        assert invalid_search_message.is_displayed(), "Invalid search message is not displayed"




    def test_auto_suggestions(self):

        search_icon = self.search_icon_input
        search_icon.click()
        time.sleep(2)

        search_input = self.serach_bar_inputfield
        search_input.clear()
        search_input.send_keys("Sunscreen")
        time.sleep(2)


        wait = WebDriverWait(self.driver, 10)
        suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-group.searchUlGroup a")))

        assert len(suggestions) >= 10

        logging.info(f"Total suggesrions found: {len(suggestions)}")

        # logging.info(suggestions.text)
        for item in suggestions:
            logging.info(item.text)
            if "The Derma Co. 1% Hyaluronic Sunscreen Aqua Gel 50gm" in item.text:
                item.click()
                break

        time.sleep(5)
        logging.info("Auto-suggestions test passed: At least 10 suggestions are displayed")


