from typing import final
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


browser = webdriver.Chrome()
def fncTest(self):
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_class input[required]")
    input1.send_keys("Ash")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second_class input[required]")
    input2.send_keys("Spring")
    input3 = browser.find_element(By.CSS_SELECTOR, ".third_class input[required]")
    input3.send_keys("ashspring@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    return self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

class TestFrom(unittest.TestCase):
    def test_registration_form1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        registration_check1 = fncTest(self)
        time.sleep(5)
        browser.quit()


    def test_registration_form2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        registration_check2 = fncTest(self)
        time.sleep(5)
        browser.quit()

if __name__ == "__main__":
    pytest.main()

