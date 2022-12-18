from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    picture = browser.find_element(By.ID, "treasure")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = picture.get_attribute("valuex")

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#



# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".