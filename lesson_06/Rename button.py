from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("http://uitestingplayground.com/textinput")

driver.maximize_window()

rename = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

rename.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(content)

driver.quit()
