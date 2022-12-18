# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # вывести ответ Степика в консоль
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#