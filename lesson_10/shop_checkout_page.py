from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса CheckoutPage.
        Открывает главную страницу оформления покупки.
        Устанавливает задержку 10 секунд для корректного отображения
        всех элементов страницы.

        :param driver: webdriver - объект драйвера Selenium.

        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Заполнение личных данных")
    def data_self(self, first_name: str, last_name: str, zip_code: str) -> None:  # noqa
        """
        Заполняет форму личных данных и нажимает
        кнопку 'Continue', дождавшись её кликабельности.

        :param first_name: str - имя.
        :param last_name: str - фамилия.
        :param zip_code: str - почтовый индекс.

        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.wait.until(EC.element_to_be_clickable(
                                        (By.ID, "continue"))).click()

    @allure.step("Получение общей стоимости")
    def get_total(self) -> str:
        """
        Получает общую стоимость товаров в корзине

        :return total: str - общая стоимость товаров в корзине.

        """
        total = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))
            ).text.split()[1]
        return total

    @allure.step("Закрытие страницы браузера")
    def close_driver(self) -> None:
        """
        Завершает сессию после окончания тестирования

        """
        self.driver.quit()
