from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import pyperclip
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)

button = browser.find_element(By.ID, "book")
# говорим Selenium проверять в течение 12 секунд, пока не появится текст на элементе
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
# пока кнопка не станет кликабельной
    #EC.element_to_be_clickable((By.ID, "verify"))
)
button.click()

browser.execute_script("window.scrollBy(0, 150);")

# взять значение и вычислить решение
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
decision = calc(x)
# вставить решение в поле
input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(decision)
# Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()
time.sleep(3)

# считать данные с окна
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
print(addToClipBoard)
pyperclip.copy(addToClipBoard)

time.sleep(3)
alert.accept()
time.sleep(3)
#browser.close()
browser.quit()