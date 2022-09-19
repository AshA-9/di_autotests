from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"
values = "Schneller!"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for element in elements:
        values = ('Ocean', ' of the Dark')
        element.send_keys(values)

    button = browser.find_element(By.XPATH, "//button[text() = 'Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
