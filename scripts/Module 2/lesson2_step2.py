from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = ""

try:
    browser = webdriver.Chrome()
    browser.get(link)



finally:
    time.sleep(5)
    browser.quit()
