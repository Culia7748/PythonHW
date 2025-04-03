from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input_name = driver.find_element (By.CSS_SELECTOR, "#newButtonName")
input_name.send_keys("SkyPro")

blue_button = driver.find_element (By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

text = blue_button.text
print(text)

driver.quit()