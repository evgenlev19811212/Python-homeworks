from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():

    driver = webdriver.Edge()

    driver.implicitly_wait(10)

    waiter = WebDriverWait(driver, 5)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
               )

    driver.maximize_window()

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    waiter.until(EC.element_to_be_clickable
                 ((By.CSS_SELECTOR, '[type="submit"]'))).click()

    fields = ["zip-code", "first-name", "last-name", "address", "e-mail",
              "phone", "city", "country", "job-position", "company"]

    for field in fields:
        attr = driver.find_element(By.ID, field).get_attribute("class")
        if field == "zip-code":
            assert attr == "alert py-2 alert-danger"
            print("Поле Zip code подсвечено красным")
        else:
            assert attr == "alert py-2 alert-success"
            print("Поле подсвечено зелёным")

    driver.quit()
