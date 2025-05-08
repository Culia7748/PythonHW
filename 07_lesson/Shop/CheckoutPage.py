from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver): #конструктор вызывается при создании нового класса
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    