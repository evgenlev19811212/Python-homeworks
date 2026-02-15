from selenium import webdriver
from shop_auth_page import AuthPage
from shop_main_page import MainPage
from shop_cart_page import CartPage
from shop_checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    auth_page = AuthPage(driver)
    auth_page.send_login("standard_user")
    auth_page.click_login()

    main_page = MainPage(driver)
    main_page.add_to_card("Sauce Labs Backpack")
    main_page.add_to_card("Sauce Labs Bolt T-Shirt")
    main_page.add_to_card("Sauce Labs Onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
            ]
    assert cart_items == expected_items, (
        "Товары в корзине не соответствуют заявленным")
    items_coumt = cart_page.check_items_count()
    expected_count = "3"
    assert items_coumt == expected_count, (
        f"Товаров в корзине {items_coumt}, а должно быть {expected_count}")
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.data_self("Евгений", "Киселев", "622001")
    to_pay = checkout_page.get_total()
    expected_pay = "$58.29"
    checkout_page.close_driver()
    assert to_pay == expected_pay, (
        f"К оплате {to_pay}, а должно быть {expected_pay}")
