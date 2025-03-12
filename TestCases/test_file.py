import time

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.jeevee.com/')


create_account = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[1]'))
)

login = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div[9]'))
)

actions = ActionChains(driver)
actions.move_to_element(create_account).move_to_element(login).click().perform()
time.sleep(10)
# except selenium.common.exceptions.TimeoutException:
#     print("Element not found within the given time frame")
# finally:
#     driver.quit()