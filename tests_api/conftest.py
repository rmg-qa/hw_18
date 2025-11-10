import allure
import pytest
from selene import browser
import requests
import data
import os
from dotenv import load_dotenv


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
    load_dotenv()
    my_email = os.getenv('MY_EMAIL')
    my_password = os.getenv('MY_PASSWORD')
    request = requests.post(data.URL + 'login',
                            json={"email": my_email, "password": my_password,
                                  "RememberMe": False},
                            allow_redirects=False)
    cookie = request.cookies.get("NOPCOMMERCE.AUTH")
    browser.open(data.URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH",
                               "value": cookie})
    browser.open(data.URL)
    return cookie
