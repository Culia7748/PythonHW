from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage

def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calc_page = CalcPage(browser)
    calc_page.delay_input(5)
    calc_page.click_button('7')
    calc_page.click_button('+')
    calc_page.click_button('8')
    calc_page.click_button('=')

    result_text = calc_page.calc_result()
    sleep(5)
    assert result_text == '15', f"expected result '15', but opened '{result_text}'"

    browser.quit()
