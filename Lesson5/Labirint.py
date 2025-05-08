# зайти на лабиринт
# найти книги по названию Python
# собрать все карточки товаров
# вывести в консоль инфо: название + автор + цена

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.labirint.ru")

search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")

search_input.send_keys("Python", Keys.RETURN)
books = driver.find_elements(By.CSS_SELECTOR, "div.product")
print(len(books))

for book in books:
    author = ''
    try:
        author = book.find_element(By.CSS_SELECTOR,'div.product-author').text
    except:
        author = 'Автор не указан'
    print(author)


sleep(3)