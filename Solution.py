import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    browser.execute_script("arguments[0].scrollIntoView(true);", book_button)
    price = browser.find_element(By.CSS_SELECTOR, "#price")
    price_100 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))

    book_button.click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(calc(x.text))
    browser.find_element(By.CSS_SELECTOR, "[type='Submit']").click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
