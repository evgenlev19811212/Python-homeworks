from selenium import webdriver
from shop_auth_page import AuthPage
from shop_main_page import MainPage
from shop_cart_page import CartPage
from shop_checkout_page import CheckoutPage
import allure


@allure.title("Тестирование магазина")
@allure.description("Тест проверяет корректность работы магазина:"
                    "авторизацию, выбор товаров и помещение их в корзину,"
                    "заполнение личных данных и вывод общей стоимости покупки")
@allure.feature("Покупки")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop() -> None:
    """
    Тест проверяет выбор товаров и оформление покупки
    в интернет-магазине до вывода их общей стоимости.

    """
    driver = webdriver.Firefox()

    with allure.step("Открытие страницы авторизации"):
        auth_page = AuthPage(driver)
    with allure.step("Ввод данных"):
        auth_page.send_login("standard_user")
    with allure.step("Переход на главную страницу"):
        auth_page.click_login()

    with allure.step("Открытие главной страницы"):
        main_page = MainPage(driver)
    with allure.step("Выбор товаров и помещение их в корзину"):
        main_page.add_to_card("Sauce Labs Backpack")
        main_page.add_to_card("Sauce Labs Bolt T-Shirt")
        main_page.add_to_card("Sauce Labs Onesie")
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()

    with allure.step("Открытие корзины"):
        cart_page = CartPage(driver)
    with allure.step("Список товаров в корзине"):
        cart_items = cart_page.get_cart_items()
    with allure.step("Ожидаемый список товаров с ценами"):
        expected_items = [
            {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
            {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
            {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
                ]
    with allure.step(f"Сравнение ожидаемого {expected_items} "
                     f"и фактического {cart_items} списков"):
        assert cart_items == expected_items, (
            "Товары в корзине не соответствуют заявленным")

    with allure.step("Количество товаров в корзине"):
        items_coumt = cart_page.check_items_count()
    with allure.step("Ожидаемое количество"):
        expected_count = "3"
    with allure.step(f"Сравнение ожидаемого {expected_count} и "
                     f"фактического {items_coumt} количества"):
        assert items_coumt == expected_count, (
            f"Товаров в корзине {items_coumt}, а должно быть {expected_count}")

    with allure.step("Переход на страницу оформления покупки"):
        cart_page.checkout()

    with allure.step("Открытие страницы оформления"):
        checkout_page = CheckoutPage(driver)
    with allure.step("Ввод личных данных"):
        checkout_page.data_self("Евгений", "Киселев", "622001")
    with allure.step("Сумма к оплате"):
        to_pay = checkout_page.get_total()
    with allure.step("Ожидаемая сумма"):
        expected_pay = "$58.29"

    with allure.step(f"Сравнение ожидаемой {expected_pay} "
                     f"и фактической суммы {to_pay}"):
        assert to_pay == expected_pay, (
            f"К оплате {to_pay}, а должно быть {expected_pay}")

    with allure.step("Завершение сессии"):
        checkout_page.close_driver()
