from selenium.webdriver.common.by import By

class SearchBarLocators(object):

    SEARCH_ICON =(By.XPATH,'//span[@class=\'icon-search\']')
    SEARCH_INPUT_FIELD = (By.ID,'autofill-search-header')
    SEARCH_BUTTON = (By.XPATH,'//button[@title=\'Search\']')
    HOME_PAGE_ELEMENT = (By.XPATH,'//span[@itemprop=\'name\'][normalize-space()=\'Home\']')
    AUTO_SUGGESTION_ELEMENT = (By.XPATH,'//li[contains(text(),\'Dot & Key Vitamin C + E Super Bright Sunscreen Spf\')]')


