from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

cookie = {"name": "cookie_policy", "value": "1"}  # избавиться от всплывающего окна подтверждения куки
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def open_labirint():
    # Открыть лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # Найти все книги со словом Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
    # Добавить все книги в корзину (_btn.btn-tocart.buy-link) тег кнопки "в корзину"
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter

def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Проверить, что счетчик товаров соответствует кол-ву добавленных книг
    #     проверить кол-во книг
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    #     сравнить его с counter
    return int(txt.split()[0])  # int-сравнение числа в строке

def close_driver():
    browser.quit()

def test_card_counter():
    open_labirint()  # Открываем сайт
    search("Python")  # Ищем книги по слову
    added = add_books()  # Добавляем книги и сохраняем результат в переменную
    go_to_cart()  # Идем в корзину
    cart_counter = get_cart_counter()  # Забираем значение счетчика из корзины
    assert added == cart_counter  # Сравниваем counter со счетчиком корзины
    close_driver()
