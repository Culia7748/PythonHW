from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver): #конструктор вызывается при создании нового класса
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def delay_input(self, delay): #ввод ожидания
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button): #нажать на кнопки
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def calc_result(self): # проверка результата
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result_text = self.driver.find_element(By.CLASS_NAME, "screen").text
        return int(result_text.split()[0])
