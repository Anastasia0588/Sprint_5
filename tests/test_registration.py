from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links


class TestRegistration:

    def test_registration_successful(self, driver, user):

        # переход на страницу регистрации пользователя
        driver.get(Links.REGISTRATION_PAGE)

        # ожидание загрузки страницы пока не появится кнопка "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        # регистрация пользователя
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys('Anastasiia')
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user.email)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(user.password)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание загрузки страницы пока не появится кнопка "Войти"
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # авторизация пользователя
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).clear()
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(user.email)
        driver.find_element(*Locators.PWD_AUTH_FIELD).clear()
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(user.password)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание выполнения авторизации пользователя
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        # переход в Личный Кабинет
        driver.find_element(*Locators.PROFILE_LINK).click()

        # получение адрес текущей страницы
        current_url = driver.current_url

        driver.quit()

        # проверка, что текущий адрес страницы - личный кабинет
        assert '/account' in current_url


    def test_registration_short_password_failed(self, driver, user):

        # переход на страницу регистрации пользователя
        driver.get(Links.REGISTRATION_PAGE)

        # ожидание загрузки страницы пока не появится кнопка "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        # регистрация пользователя
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys('Anastasiia')
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(user.email)
        user.password = '123'
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(user.password)

        # ожидание, что кнопка "Зарегистрироваться" кликабельна
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # получение сообщения об ошибке
        error_msg = driver.find_element(*Locators.WRONG_PASSWORD_TEXT).text

        # получение адрес текущей страницы
        current_url = driver.current_url

        driver.quit()

        # проверка, что текущий адрес страницы - личный кабинет
        assert '/register' in current_url and error_msg == 'Некорректный пароль'
