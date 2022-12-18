# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# модуль для загрузки файлов
import os

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Anastasia")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Molchanova")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("bro@gmail.com")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым

    # получаем путь к директории текущего исполняемого скрипта
    current_dir = os.path.abspath(os.path.dirname("lesson2_step8_loadFile.py"))

    # имя файла, который будем загружать на сайт
    file_name = "file.txt"

    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    print(file_path)

    # отправляем файл
    input = browser.find_element(By.ID, "file")
    input.send_keys(file_path)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#пустая строка, чтобы последняя строка кода прочиталась
