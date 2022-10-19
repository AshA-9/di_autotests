from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
def calc(str_answer):
    return str(answer)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Taking inputs and calculating answer
    input1 = browser.find_element(By.ID, "num1")
    value1 = input1.text
    value1_answer = int(value1)

    input2 = browser.find_element(By.ID, "num2")
    value2 = input2.text
    value2_answer = int(value2)

    answer = value1_answer + value2_answer
    str_answer = calc(answer)

    # Searching for answer from dropdown list
    select_answer = Select(browser.find_element(By.TAG_NAME, "select"))
    select_answer.select_by_visible_text(str_answer)

    # Click 'submit' button
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
