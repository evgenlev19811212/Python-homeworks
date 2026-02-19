from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_card(self, product_name):
        productname = product_name.replace(" ", "-").lower()
        id = f'add-to-cart-{productname}'
        self.wait.until(EC.element_to_be_clickable((By.ID, id))).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
