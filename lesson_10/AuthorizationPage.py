from selenium.webdriver.common.by import By
import  allure

class AuthorizationPage:
    def __init__(self, driver):
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
            внутри экземпляра класса. Создает экземпляр ожидания элементов со страницы.
            Раскрывает окно браузера на максимальный размер.
            :param driver:
                """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    @allure.step("Авторизоваться, используя логин {user_name} и пароль {password}")
    def authorization(self, user_name, password ):
        """Метод находит по локатору поля для заполнения формы авторизации и заполняет их нужными значениями.
        :param user_name: str
        :param password: str"""
        self.driver.find_element(By.ID, "user-name").send_keys(user_name)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()