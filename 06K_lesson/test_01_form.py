from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
   driver = webdriver.Chrome()

   driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

   driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="first-name"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="last-name"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="address"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="e-mail"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="phone"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="city"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="country"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="job-position"]')))

   driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
   WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, '[name="company"]')))

   driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

   zip_code_input = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
   assert zip_code_input == "alert py-2 alert-danger"

   #if zip_code_input == "alert py-2 alert-danger":
     # print("Zip code красный")
 #  else: print("Zip code ошибка")

   colors = ["#first-name", "#last-name", "#address", "#city",
             "#country", "#e-mail", "#phone", "#job-position", "#company"]
   for color in colors:
      color = driver.find_element(By.CSS_SELECTOR, color).get_attribute("class")
      assert color == "alert py-2 alert-success"
      # if color == "alert py-2 alert-success" :
      #    print("Остальные все зелёный")
      # else: print("Ошибка")

   driver.quit()