from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = ("http://suninjuly.github.io/explicit_wait2.html")
def calculation(input_value):
    return str(math.log(abs(12*math.sin(int(input_value)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Checking booking price
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    take_value = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", take_value)
    input_value = take_value.text
    answer = calculation(input_value)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button#solve").click()

finally:
    time.sleep(5)
    browser.quit()

