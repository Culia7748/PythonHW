import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome()
    #(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    #авторизация пользователя
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    #добавление товара в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    #перейти в корзину
    driver.find_element(By.ID, "shopping_cart_container").click()

    #нажать checkout
    driver.find_element(By.ID, "checkout").click()

    #заполнение формы данными
    driver.find_element(By.ID, "first-name").send_keys("Юлия")
    driver.find_element(By.ID, "last-name").send_keys("Цыганкова")
    driver.find_element(By.ID, "postal-code").send_keys("413370")

    #нажать кнопку continue
    driver.find_element(By.ID, "continue").click()

    #прочитать со страницы итоговую стоимость
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total = total_price.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total
    print(f"Итоговая сумма равна ${total}")

    driver.quit()