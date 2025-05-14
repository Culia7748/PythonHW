import allure
from selenium.webdriver.common.by import By
import  allure

class CheckoutPage:

    def __init__(self, driver):
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                внутри экземпляра класса. Создает экземпляр ожидания элементов со страницы.
                Раскрывает окно браузера на максимальный размер.
                :param driver:
                    """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    @allure.step("Нажать на кнопку 'checkout'")
    def checkout(self):
        """Поиск кнопки 'checkout' по локатору и клукнуть её"""
        self.driver.find_element(By.ID, "checkout").click()