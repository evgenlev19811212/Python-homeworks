from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class AuthPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса AuthPage.
        Открывает и максимизирует страницу авторизации магазина.
        Устанавливает неявное ожидание для корректного отображения
        всех элементов страницы.

        :param driver: webdriver — объект драйвера Selenium.

        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @allure.step("Авторизация")
    def send_login(self, username: str, password: str = "secret_sauce") -> None:  # noqa
        """
        Вводит логин и пароль для авторизации.

        :param username: str — имя пользователя.
        :param password: str — пароль (задан по умолчанию,
        т.к. для тестов используется один пароль для всех пользователей).
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Переход на главную страницу")
    def click_login(self) -> None:
        """
        Осуществляет переход на главную страницу.

        """
        self.driver.find_element(By.ID, "login-button").click()
