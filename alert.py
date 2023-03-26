import time
import math
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# Открыть страницу
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

# Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()
time.sleep(1)

# Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

# взять значение и вычислить решение
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
decision = calc(x)
# втавить решение в поле
input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(decision)
# Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()
time.sleep(3)

# считать данные с окна
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
print(addToClipBoard)
pyperclip.copy(addToClipBoard)



time.sleep(5)
#browser.close()
browser.quit()