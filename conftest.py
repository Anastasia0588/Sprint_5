import random

import pytest
from selenium import webdriver

import helper
from data import User


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()

    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--headless')  # добавили настройку
    chrome_options.add_argument('--window-size=1024,768')  # добавили ещё настройку

    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = User(name='Anastasiia')
    user.email = f'anastasiiadrozdovskaia5{random.randint(1000, 9999)}@autotest.ru'
    user.password = helper.gen_password()
    return user
