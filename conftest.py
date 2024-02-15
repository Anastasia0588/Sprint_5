import pytest
from selenium import webdriver
import random
import string
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
def user(gen_password):
    user = User(name='Anastasia')
    user.email = f'anastasiiadrozdovskaia5{random.randint(1000, 9999)}@autotest.ru'
    user.password = gen_password
    return user

@pytest.fixture
def gen_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(6))
    return password