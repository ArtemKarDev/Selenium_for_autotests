import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL1 = "http://suninjuly.github.io/registration1.html"
URL2 = "http://suninjuly.github.io/registration2.html"
need_text = "Congratulations! You have successfully registered!"
class UniqSelect(unittest.TestCase):
    def test_uniq_select1(self):
        self.assertEqual(browserStart(URL1), need_text, 'Text matched')

    def test_uniq_select2(self):
        self.assertEqual(browserStart(URL2), need_text, 'Text matched')

def browserStart(URL):
    browser = webdriver.Chrome()
    browser.get(URL)

    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
    input3.send_keys("@@@@@")
    input4 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control first"]')
    input4.send_keys("4634563456")
    input5 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control second"]')
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
    return welcome_text


if __name__ == "__main__":
    unittest.main()