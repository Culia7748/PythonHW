import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver):
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                внутри экземпляра класса. Создает экземпляр ожидания элементов со страницы.
                Раскрывает окно браузера на максимальный размер.
                :param driver:
                    """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Ввести время ожидания результата со значением {delay}")
    def delay_input(self, delay):
        """Метод находит необходимый элемент страницы по локатору для ввода нужного значения времени ожидания.
        :param delay: int
        Предварительно поле нужно очистить от предыдущего значения."""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажать на кнопки с нужными математическими значениями {button}")
    def click_button(self, button):
        """Метод ищет кнопки с заданным текстовым значением в названии локатора кнопки и нажимает на них
        :param button: str"""
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Получить результат с экрана калькулятора")
    def calc_result(self):
        """Метод получения результата с экрана калькулятора с ипользованием механизма ожидания
            для задержки выполнения дальнейших шагов (46с), пока не появится указанный текст (15) в нужном элементе.
            Возвращает результат с экрана, преобразуя его в числовое значение"""
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result_text = self.driver.find_element(By.CLASS_NAME, "screen").text
        return int(result_text.split()[0])