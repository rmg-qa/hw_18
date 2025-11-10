import allure
import requests
from selene import browser
import data


class Cart:

    @allure.title('Очистка корзины')
    def del_cart(self):
        browser.element(".//span[text()='Shopping cart']").click()
        browser.element("[name='removefromcart']").click()
        browser.element('[value="Update shopping cart"]').click()

    @allure.title('Добавление товара в корзину')
    def add_item_in_cart(self, payload, cookie):
        request = requests.post(data.URL + "addproducttocart/details/2/1",
                                data=payload,
                                cookies={"NOPCOMMERCE.AUTH": cookie})
        return request
