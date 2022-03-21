from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#input_value')
    x=int(x_element.text)
    y=log(abs(12 * sin(x)))
    input_element = browser.find_element_by_css_selector('#answer')
    input_element.send_keys(str(y))
    check = browser.find_element_by_id('robotCheckbox')
    check.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
