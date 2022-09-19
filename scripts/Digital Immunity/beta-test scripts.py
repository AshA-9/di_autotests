from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://192.168.1.31/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Login page
    


finally:
    time.sleep(10)
    browser.quit()