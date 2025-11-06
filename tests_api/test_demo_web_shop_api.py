import logging
from selene import browser, have
import allure
import data
from classes.cart import Cart
from classes.allure import Allure


@allure.title('Проверка добавления товара в корзину')
@allure.description("Делаю заказ и проверяю, что он добавился в корзину, затем через UI очищаю корзину. "
                    "Через запрос это сделать очень сложно из-за реализации запроса cart.")
def test_add_item_in_cart(browser_settings, get_cookie_auth):
    cookie = get_cookie_auth
    Allure.loginning_allure_request_json(data.request_body, name="Request")  # логирование request в Allure
    result = Cart.add_item_in_cart(payload=data.request_body, cookie=cookie)
    Allure.loginning_allure_response_json(result, name="Response")  # логирование response в allure
    logging.info(result.status_code)  # логирование в консоль
    browser.driver.refresh()  # обновляю страницу, так как webdriver ведет себя нестабильно после возврата кук
    # в фикстуре get_cookie_auth. Иногда мог падать
    browser.element(".//span[@class='cart-qty']").should(have.text("(1)"))
    Cart.del_cart()
    assert browser.element("[class='order-summary-content']").should(have.text("Your Shopping Cart is empty!"))


@allure.title('Проверка добавления 3 одинаковых товаров в корзину')
@allure.description("Делаю заказ с параметром 'addtocart_2.EnteredQuantity'= 3, и проверяю, "
                    "что это количество и добавилось. В конце очищаю корзину")
def test_add_2_identical_items_in_cart(browser_settings, get_cookie_auth):
    cookie = get_cookie_auth
    data.request_body["addtocart_2.EnteredQuantity"] = "3"  # меняем количество товара на 3
    Allure.loginning_allure_request_json(data.request_body, name="Request")  # логирование request в Allure
    result = Cart.add_item_in_cart(payload=data.request_body, cookie=cookie)
    Allure.loginning_allure_response_json(result, name="Response")  # логирование allure
    logging.info(result.status_code)  # логирование в консоль
    browser.driver.refresh()  # обновляю страницу, так как webdriver ведет себя нестабильно
    # после возврата кук в фикстуре get_cookie_auth. Иногда мог падать
    browser.element(".//span[@class='cart-qty']").should(have.text("(3)"))
    Cart.del_cart()
    assert browser.element("[class='order-summary-content']").should(have.text("Your Shopping Cart is empty!"))
