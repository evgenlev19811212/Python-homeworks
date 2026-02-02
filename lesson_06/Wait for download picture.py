from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

waiter = WebDriverWait(driver, 30)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
           )
driver.maximize_window()

waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))

attribute = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(attribute)

driver.quit()
