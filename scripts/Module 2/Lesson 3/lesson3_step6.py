from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calculation(input_value):
    return str(math.log(abs(12*math.sin(int(input_value)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

    # Going to new window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Getting through captcha
    take_value = browser.find_element(By.ID, "input_value")
    input_value = take_value.text
    answer = calculation(input_value)
    print(take_value)
    print(answer)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
