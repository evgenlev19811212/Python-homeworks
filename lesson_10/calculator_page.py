from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса CalcPage.
        Открывает и максимизирует страницу калькулятора.

        :param driver: webdriver — объект драйвера Selenium.

        """
        self.driver = driver
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    @allure.step("Установка задержки {delay} секунд")
    def delay(self, delay: int) -> None:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        seconds = self.driver.find_element(By.ID, "delay")
        seconds.clear()
        seconds.send_keys(delay)

    @allure.step("Нажатие кнопки '{button}'")
    def click_button(self, button: str) -> None:
        """
        Нажимает на кнопку калькулятора.

        :param button: str — текст на кнопке, которую нужно нажать.
        """
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Получение результата с экрана калькулятора")
    def result(self, result: str, delay: int) -> str:
        """
        Ожидает появления результата на экране калькулятора.
        Возвращает текущий результат с экрана калькулятора.

        :param result: str — ожидаемый результат.
        :param delay: int — время задержки в секундах.
        :return get_result: str — текст результата на экране калькулятора.
        """
        # Добавляем +1 секунду к задержке для надежности
        self.wait = WebDriverWait(self.driver, delay + 1)
        self.wait.until(EC.text_to_be_present_in_element((
            By.CLASS_NAME, "screen"), result))
        get_result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return get_result

    @allure.step("Закрытие страницы калькулятора")
    def close_driver(self) -> None:
        """
        Завершает сессию после окончания тестирования

        """
        self.driver.quit()
