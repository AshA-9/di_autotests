from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://hpstore.uz/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    add_button = browser.find_element(By.CSS_SELECTOR, )
    add_button.click()
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()
    browser.get("https://fake-shop.com/basket.html")
    goods = browser.find_elements(By.CSS_SELECTOR, ".good")
    assert len(goods) == 2

finally:
    time.sleep(10)
    browser.quit()
