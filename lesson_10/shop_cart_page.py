from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса CartPage.
        Открывает страницу корзины.
        Устанавливает задержку 10 секунд для корректного отображения
        всех элементов страницы.

        :param driver: webdriver — объект драйвера Selenium.

        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Получение списка товаров в корзине")
    def get_cart_items(self) -> list:
        """
        Получает список товаров в корзине с указанием названий и цен.

        :return items: list — список товаров в корзине
          с указанием названий и цен.
        """
        items = []
        cart_item_elements = self.driver.find_elements(
                            By.CLASS_NAME, 'cart_item')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})
        return items

    @allure.step("Получение количества товаров в корзине")
    def check_items_count(self) -> str:
        """
        Получает количество товаров в корзине.

        :return items_count: str — количество товаров в корзине
          с указанием названий и цен.
        """
        items_count = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_badge"))).text
        return items_count

    @allure.step("Переход на страницу оформления покупки")
    def checkout(self) -> None:
        """
        Осуществляет переход на страницу оформления покупки.

        """
        self.driver.find_element(By.ID, "checkout").click()
