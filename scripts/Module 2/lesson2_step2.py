from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter import *
import tkinter

# link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"
link = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "select#cars").click()
    browser.find_element(By.CSS_SELECTOR, "[value = 'audi']").click()
    press_button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    press_button.click()

finally:
    time.sleep(5)
    browser.quit()
