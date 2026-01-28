from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

input_element = driver.find_element(By.CSS_SELECTOR, 'input')

input_element.send_keys("Sky")

sleep(5)

input_element.clear()

input_element.send_keys("Pro")

sleep(5)

driver.quit()
