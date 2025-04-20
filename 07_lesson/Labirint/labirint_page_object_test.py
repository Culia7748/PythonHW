from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#Импотируем класс из файла MainPage, который лежит в папке pages:
from Pages.MainPage import MainPage
from Pages.ResultPage import ResultPage
from Pages.CartPage import CartPage

def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
    main_page.set_cookie_policy() #Вызываем метод set_cookie_policy из MainPage
    main_page.search("paython")

    result_page = ResultPage(browser) #Переменная хранит экземпляр класса ResultPage
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.go_to_cart()
    as_is = cart_page.get_cart_counter()

    assert as_is == to_be

    browser.quit()

def test_empty_search():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
    main_page.set_cookie_policy() #Вызываем метод set_cookie_policy из MainPage
    main_page.search("no book search term")

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()