from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 20, 0.1)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#text.lead"), "Done!")
)

src = driver.find_element(By.CSS_SELECTOR, '[src="img/award.png"]').get_attribute("src")

print("src атрибут 3-ей картинки:", src)

driver.quit()