from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса MainPage.
        Открывает главную страницу магазина.
        Устанавливает задержку 10 секунд для корректного отображения
        всех элементов страницы.

        :param driver: webdriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Добавление товара в корзину")
    def add_to_card(self, product_name: str) -> None:
        """
        Добавляет товар в корзину.

        :param product_name: str - название товара
        """
        productname = product_name.replace(" ", "-").lower()
        id = f'add-to-cart-{productname}'
        self.wait.until(EC.element_to_be_clickable((By.ID, id))).click()

    @allure.step("Переход на страницу корзины")
    def go_to_cart(self) -> None:
        """
        Осуществляет переход на страницу корзины.

        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
