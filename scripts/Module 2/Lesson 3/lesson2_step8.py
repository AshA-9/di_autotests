import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ash")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Yellow")

    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("yellow@proton.com")

    # Clicking on 'Choose File' and sending .txt file

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'autotest.txt')
    upload_file = browser.find_element(By.ID, "file")
    upload_file.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
