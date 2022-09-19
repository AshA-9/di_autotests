from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"
link = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    select = Select(browser.find_element(By.ID, "cars"))
    select.select_by_value("2") # searching element 1

    press_button = browser.find_element(By.CSS_SELECTOR, "[type = "submit"]")

finally:
    time.sleep(5)
    browser.quit()
