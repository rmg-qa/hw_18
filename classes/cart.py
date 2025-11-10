import allure
import requests
from selene import browser

import data


class Cart:

    @allure.step('Добавляем товары в корзину')
    def add_item_in_cart(self, payload, cookie):
        request = requests.post(data.URL + "addproducttocart/details/2/1",
                                data=payload,
                                cookies={"NOPCOMMERCE.AUTH": cookie})
        return request

    @allure.step('Удаляем товары в корзине')
    def del_cart(self):
        browser.element(".//span[text()='Shopping cart']").click()
        browser.element("[name='removefromcart']").click()
        browser.element('[value="Update shopping cart"]').click()
