from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
decision = calc(x)
print(decision)

browser.execute_script("window.scrollBy(0, 150);")

input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(decision)

browser.find_element(By.CSS_SELECTOR, "input[type=checkbox]").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


time.sleep(8)
browser.close()
browser.quit()