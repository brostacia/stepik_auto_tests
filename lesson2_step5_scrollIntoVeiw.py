from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	browser.execute_script("window.scrollBy(0, 300);")
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # # закрываем браузер после всех манипуляций
    browser.quit()

#