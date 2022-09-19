from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_class input[required]")
    input1.send_keys("Ash")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second_class input[required]")
    input2.send_keys("Spring")
    input3 = browser.find_element(By.CSS_SELECTOR, ".third_class input[required]")
    input3.send_keys("ashspring@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
