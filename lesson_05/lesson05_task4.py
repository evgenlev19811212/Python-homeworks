from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

driver.maximize_window()

username = driver.find_element(By.CSS_SELECTOR, "#username")

username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "#password")

password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, ".radius")

login_button.click()

text = driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success")

print(text.text)

sleep(5)

driver.quit()
