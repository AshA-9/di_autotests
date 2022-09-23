from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calculation(input_value):
    return str(math.log(abs(12*math.sin(int(input_value)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Taking #input_value to evaluate 'x'
    x_input = browser.find_element(By.ID, "input_value")
    input_value = x_input.text
    answer = calculation(input_value)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer)

    # Marking robotCheckbox and scrollIntoView
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # browser.execute_script("window.scrollBy(0, 100);")

    radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    # Click 'submit' button
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

finally:
    time.sleep(7)
    browser.quit()
