import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)
print(current_dir)
print(file_path)
#print(os.path.abspath(os.path.dirname(__file__)))
#print(os.path.abspath(__file__))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("qwerty")
browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("asdfasdf")
browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("@@@")

input_file = browser.find_element(By.CSS_SELECTOR,"input[type='file']")
input_file.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(8)
browser.close()
browser.quit()

