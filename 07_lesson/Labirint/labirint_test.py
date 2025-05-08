from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

cookie = {"name": "cookie_policy", "value": "1"}  # избавиться от всплывающего окна подтверждения куки


def test_card_counter():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    # Открыть лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    # Найти все книги со словом Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    # Добавить все книги в корзину (_btn.btn-tocart.buy-link) тег кнопки "в корзину"
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    print(counter)

    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")
    # Проверить, что счетчик товаров соответствует кол-ву добавленных книг
    #     проверить кол-во книг
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    #     сравнить его с counter
    assert counter == int(txt.split()[0]) #int-сравнение числа в строке
    browser.quit()
