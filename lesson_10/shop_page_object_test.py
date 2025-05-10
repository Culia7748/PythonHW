from time import sleep

import  pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from AuthorizationPage import AuthorizationPage
from MainShopPage import MainShopPage
from CheckoutPage import CheckoutPage
from InformationPage import InformationPage
import  allure

@pytest.fixture
def driver():
    """Используется фикстура Pytest для инициализации и завершения работы браузера."""
    chrome_options = Options()
    """Отключаем автозаполнение паролей и выключаем менеджер паролей"""
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    """Установка драйвера Chrome и запуск браузера"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    options = chrome_options
    """Максимизируем окно браузера"""
    driver.maximize_window()
    """Ждем до 20 секунд появления элементов страницы"""
    driver.implicitly_wait(20)
    """Возвращаем драйвер тестовым методам"""
    yield driver
    """Завершаем работу браузера после всех тестов"""
    driver.quit()

@allure.epic("Магазин")
@allure.severity("blocker")
@allure.title("Заказ товара на сайте магазина")
@allure.description("Тест предназнаен для заказа нескольких позиций товара и получения итоговой суммы заказа")


def test_shop(driver):
    authorization = AuthorizationPage(driver)
    authorization.authorization("standard_user", "secret_sauce")

    main_shop_page = MainShopPage(driver)
    main_shop_page.add_product()
    main_shop_page.get_shopping_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout()

    information_form = InformationPage(driver)
    information_form.information_form("Юлия", "Цыганкова", "413370")
    information_form.cont()

    total = information_form.total_price()
    expected_total = "58.29"
    with allure.step("Сравнение ожидаемой суммы с суммой результата тестирования"):
        assert total == expected_total