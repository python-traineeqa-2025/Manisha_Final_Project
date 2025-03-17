from Page_Objects.SearchBar.SearchLocators import SearchBarLocators

class Search_Bar_Properties(SearchBarLocators):

    @property
    def search_icon_input(self):
        return self.driver.find_element(*SearchBarLocators.SEARCH_ICON)

    @property
    def serach_bar_inputfield(self):
        return self.driver.find_element(*SearchBarLocators.SEARCH_INPUT_FIELD)

    @property
    def search_button(self):
        return self.driver.find_element(*SearchBarLocators.SEARCH_BUTTON)

    @property
    def home_page_element(self):
        return self.driver.find_element(*SearchBarLocators.HOME_PAGE_ELEMENT)

    # @property
    # def autosuggestion(self):
    #     return self.driver.find_element(*SearchBarLocators.AUTO_SUGGESTION_ELEMENT)