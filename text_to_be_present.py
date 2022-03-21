from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    button1 = browser.find_element_by_css_selector('#book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    button1.click()
    x_element = browser.find_element_by_css_selector('#input_value')
    x=int(x_element.text)
    y=log(abs(12 * sin(x)))
    input_element = browser.find_element_by_css_selector('#answer')
    input_element.send_keys(str(y))
    button2 = browser.find_element_by_css_selector("#solve")
    button2.click()
finally:
    time.sleep(10)
    browser.quit()

