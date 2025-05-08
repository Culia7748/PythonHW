from selenium.webdriver.common.by import By

class MainShopPage:

    def __init__(self, driver): #конструктор вызывается при создании нового класса
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def add_product(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def get_shopping_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()