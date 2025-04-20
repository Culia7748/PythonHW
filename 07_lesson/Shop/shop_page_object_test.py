from time import sleep
import  pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from AuthorizationPage import AuthorizationPage
from MainShopPage import MainShopPage
from CheckoutPage import CheckoutPage
from InformationPage import InformationPage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    options = chrome_options
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

def test_shop(driver):
    authorization = AuthorizationPage(driver)
    authorization.authorization("standard_user", "secret_sauce")

    sleep(5)

    main_shop_page = MainShopPage(driver)
    main_shop_page.add_product()
    main_shop_page.get_shopping_cart()

    sleep(5)

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout()

    information_form = InformationPage(driver)
    information_form.information_form("Юлия", "Цыганкова", "413370")
    information_form.cont()

    sleep(5)

    total = information_form.total_price()
    #total = total_price.text.strip().replace("Total: $", "")
    expected_total = "58.29"
    assert total == expected_total
