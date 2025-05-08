from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self.driver = browser

    def go_to_cart(self):
        # Перейти в корзину
        self.driver.get("https://www.labirint.ru/cart/")

    def get_cart_counter(self):
        # Проверить, что счетчик товаров соответствует кол-ву добавленных книг
        #     проверить кол-во книг
        txt = self.driver.find_element(By.ID, 'basket-default-prod-count2').text
        #     сравнить его с counter
        return int(txt.split()[0])  # int-сравнение числа в строке