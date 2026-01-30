from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get("http://www.uitestingplayground.com/ajax")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, ".bg-success").text

print(content)

driver.quit()
