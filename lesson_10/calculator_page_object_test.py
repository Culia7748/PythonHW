from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage
import  allure

@allure.epic("Калькулятор")
@allure.severity("blocker")
@allure.title("Калькулятор чисел")
@allure.description("Проведение математических операций с помощью калькулятора и получение результата")
def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calc_page = CalcPage(browser)
    calc_page.delay_input(45)
    calc_page.click_button('7')
    calc_page.click_button('+')
    calc_page.click_button('8')
    calc_page.click_button('=')

    result_text = calc_page.calc_result()

    with allure.step("Сравнить значение результата с экрана калькулятора с ожидаемым значением"):
        assert result_text == 15, f"expected result '15', but opened '{result_text}'"

    browser.quit()