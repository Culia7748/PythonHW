from selenium.webdriver.common.by import By

class InformationPage:

    def __init__(self, driver): #конструктор вызывается при создании нового класса
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def information_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def cont(self):
        self.driver.find_element(By.ID, "continue").click()

    def total_price(self):
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total = total_price.text.strip().replace("Total: $", "")
        #return int(total_price.split()[0])
