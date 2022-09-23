from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# current file's directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# adding to path file's name
file_path = os.path.join(current_dir, 'lesson2_step6.py')

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
