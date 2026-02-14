from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_cart_items(self):
        items = []
        cart_item_elements = self.driver.find_elements(
                            By.CLASS_NAME, 'cart_item')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})
        return items

    def check_items_count(self):
        items_count = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_badge"))).text
        return items_count

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
