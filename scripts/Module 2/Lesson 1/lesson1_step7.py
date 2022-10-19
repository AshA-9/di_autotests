
# Playing around with get_attribute() method

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x_value):
    return str(math.log(abs(12*math.sin(int(x_value)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # taking given input, calculate input with calc() function and give it to 'answer' variable
    math_check = browser.find_element(By.ID, "treasure")
    x_value = math_check.get_attribute("valuex")
    print("value of x_value: ", x_value)
    answer = calc(x_value)

    # send calculated 'answer' to input field
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer)

    # click on checkbox and radio buttons, and click submit button
    checkbox_button = browser.find_element(By.ID, "robotCheckbox")
    checkbox_button.click()
    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()


