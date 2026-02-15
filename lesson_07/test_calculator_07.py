from selenium import webdriver
from calculator_page import CalcPage


def test_calc():
    driver = webdriver.Chrome()
    calculator = CalcPage(driver)

    calculator.delay('5')

    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    result = calculator.result('15')
    assert result == '15'

    calculator.close_driver()
