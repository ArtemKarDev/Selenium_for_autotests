import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

#link = "https://stepik.org/lesson/236895/step/1"
with open('../login.txt', 'r') as f:
    LOGIN = [line.rstrip() for line in f]
f.close()


class TestPage():

    @pytest.mark.parametrize('links', ["236895","236896","236897","236898","236899","236903","236904","236905"])
    def test_guest_should_see_basket_link(self, browser, links):

        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ember33"))).click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login']")))
        browser.find_element(By.XPATH, "//input[@name='login']").send_keys(LOGIN[0])
        browser.find_element(By.XPATH, "//input[@name='password']").send_keys(LOGIN[1])
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        #popup = browser.find_element_by_class_name("popup")

        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".box")))

        time.sleep(5)

        wait.until(EC.presence_of_element_located((By.XPATH, "//textarea"))).send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.XPATH, "//button[@class='submit-submission']").click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))

        output = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        print(output)
        if output != "Correct!":
            with open("logfile.txt", "a", encoding="utf-8") as f:  # дозаписываем в logfile
                f.write(output + " ")
        assert output == 'Correct!', 'Not Correct!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'




if __name__ == "__main__":
    pytest.main()
