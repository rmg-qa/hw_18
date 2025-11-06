import allure
import pytest
from selene import browser
import requests
import data


@allure.title('Настройки браузера. Разрешение 1920х1080')
@pytest.fixture(scope='function')
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@allure.title('Авторизация и получение cookie')
@pytest.fixture(scope='function')
def get_cookie_auth(browser_settings):
    request = requests.post(data.URL + 'login',
                            json={"email": data.email, "password": data.password, "RememberMe": False},
                            allow_redirects=False)
    cookie = request.cookies.get("NOPCOMMERCE.AUTH")
    browser.open(data.URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH",
                               "value": cookie})
    browser.open(data.URL)
    return cookie
