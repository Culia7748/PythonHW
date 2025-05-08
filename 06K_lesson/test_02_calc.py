from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration import URL_2


def test_calculator():
    chrom_browser = webdriver.Chrome()
    chrom_browser.get(URL_2)

    #время ожидания результата калькулятора
    delay_input = chrom_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)

    #7
    chrom_browser.find_element(By.XPATH, "//span[text()='7']").click()
    #+
    chrom_browser.find_element(By.XPATH, "//span[text()='+']").click()
    #8
    chrom_browser.find_element(By.XPATH, "//span[text()='8']").click()
    #=
    chrom_browser.find_element(By.XPATH, "//span[text()='=']").click()

    waiter = WebDriverWait(chrom_browser, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = chrom_browser.find_element(By.CLASS_NAME, "screen").text

    # проверка результата
    assert result_text == '15', f"expected result '15', but opened '{result_text}'"

    print("Проверка пройдена: результат", result_text)

    chrom_browser.quit()

