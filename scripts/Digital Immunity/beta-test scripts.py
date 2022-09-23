from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://192.168.1.30/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Passing through private connection issue
    browser.find_element(By.CSS_SELECTOR, "button#details-button").click()
    browser.find_element(By.ID, "proceed-link").click()

    # Login page
    login_input = browser.find_element(By.ID, "username")
    login_input.send_keys("Admin")
    psswrd_input = browser.find_element(By.ID, "pwd")
    psswrd_input.send_keys("Azzimut.123")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(6)
    browser.quit()
