from selenium import webdriver
from calculator_page import CalcPage
import allure


@allure.title("Тестирование калькулятора: 7 + 8 = 15")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Простые математические операции")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(delay: int = 5) -> None:
    """
    Тест проверяет работу калькулятора.

    :param delay: int — задержка в секундах для выполнения операции.
    """
    driver = webdriver.Chrome()
    with allure.step("Открытие страницы калькулятора"):
        calculator = CalcPage(driver)

    with allure.step(f"Установка задержки {delay} секунд"):
        calculator.delay(delay)

    with allure.step("Нажатие кнопок: 7 + 8 ="):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')

    with allure.step("Ожидание и получение результата 15"):
        result = calculator.result('15', delay)

    with allure.step("Проверка результата 15"):
        assert result == '15'

    with allure.step("Завершение сессии"):
        calculator.close_driver()
