from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
def cal(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = cal(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(answer)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']")
    checkbox.click()

    checkbox_button = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    checkbox_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

