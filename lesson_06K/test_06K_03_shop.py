from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()

    waiter = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    waiter.until(EC.element_to_be_clickable
                 ((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    waiter.until(EC.element_to_be_clickable
                 ((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    waiter.until(EC.element_to_be_clickable
                 ((By.ID, "add-to-cart-sauce-labs-onesie"))).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Евгений")
    driver.find_element(By.ID, "last-name").send_keys("Киселев")
    driver.find_element(By.ID, "postal-code").send_keys("622001")
    driver.find_element(By.ID, "continue").click()

    total = waiter.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "summary_total_label"), "Total: $58.29"))

    driver.quit()

    assert total
