from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  allure

class InformationPage:

    def __init__(self, driver):
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                внутри экземпляра класса. Создает экземпляр ожидания элементов со страницы.
                Раскрывает окно браузера на максимальный размер.
                :param driver:
                    """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    @allure.step("Заполнить форму для оформления заказа: имя {first_name}, фамилия {last_name},"
                 "индекс почтового отделения {postal_code}")
    def information_form(self, first_name, last_name, postal_code):
        """Метод находит по локатору поля для заполнения формы строковыми значениями.
        :param first_name: str
        :param last_name: str
        :param postal_code: str"""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Нажать на кнопку 'продолжить'")
    def cont(self):
        """Метод находит по локатору кнопку 'продолжить' для перехода к следующей странице"""
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму")
    def total_price(self):
        """Метод извлекает общую сумму заказа со страницы из HTML-элемента.
        Используетя механизм ожидания в 10 с. до появления элемента на странице.
        Возвращается числовое значение суммы."""
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return total_price_element.text.strip().replace("Total: $", "")