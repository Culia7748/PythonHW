from selenium.webdriver.common.by import By
import  allure

class MainShopPage:

    def __init__(self, driver):
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
               внутри экземпляра класса. Создает экземпляр ожидания элементов со страницы.
               Раскрывает окно браузера на максимальный размер.
               :param driver:
               """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    @allure.step("Добавить товар в корзину")
    def add_product(self):
        """Метод находит по локатору кнопку для добавления товара в корзину"""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.feature("Работа с товаром")
    @allure.step("Перейти в корзину")
    def get_shopping_cart(self):
        """Метод находит по локатору кнопку 'корзина' для перехода на страницу корзины с товарами"""
        self.driver.find_element(By.ID, "shopping_cart_container").click()