# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    #  Чтобы определить момент, когда цена аренды уменьшится до $100,
    #  используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
    # .text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),'$100')
        )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
        # Считать значение для переменной x.

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Нажать на кнопку
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций





# ***
# selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
# An expectation for checking if the given text is present in the specified element. locator, text