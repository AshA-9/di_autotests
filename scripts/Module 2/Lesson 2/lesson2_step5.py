# Working with 'execute_script'.
# Common problem of intercepting elements in automation tests.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
