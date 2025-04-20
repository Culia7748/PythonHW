from selenium.webdriver.common.by import By

class AuthorizationPage:

    def __init__(self, driver): #конструктор вызывается при создании нового класса
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def authorization(self, user_name, password ):
        self.driver.find_element(By.ID, "user-name").send_keys(user_name)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()