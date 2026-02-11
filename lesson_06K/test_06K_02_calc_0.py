from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()

    waiter = WebDriverWait(driver, 47)

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    driver.get(url)

    driver.maximize_window()

    seconds = driver.find_element(By.ID, "delay")
    seconds.clear()
    seconds.send_keys(45)

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    waiter.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"),
                                                  "15"))
    sum = driver.find_element(By.CLASS_NAME, "screen").text
    assert sum == "15"

    driver.quit()
