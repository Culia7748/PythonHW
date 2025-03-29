from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Открыть браузер FireFox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Перейти на страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith
username_input = driver.find_element (By.CSS_SELECTOR, "#username")
username_input.send_keys("tomsmith", Keys.RETURN)
sleep(3)

# В поле password ввести значение SuperSecretPassword!
password_input = driver.find_element (By.CSS_SELECTOR, "#password")
password_input.send_keys("SuperSecretPassword!", Keys.RETURN)
sleep(3)

# Нажать кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, ".radius")
login_button.click()

# Вывести текст с зеленой плашки в консоль
text = driver.find_element(By.CSS_SELECTOR, 'div.row  [alt="Fork me on GitHub"]').text
print(text)

# Закрыть браузер (метод quite())
driver.quit()