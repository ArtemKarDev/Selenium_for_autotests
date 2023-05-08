import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"




@pytest.fixture(autouse=True)  # параметр autouse=True,  фикстуру нужно запустить для каждого теста без явного вызова
def prepare_data():
    print()
    print("preparing some critical data for every test")

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # @pytest.mark.skip
    # @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.win10
    #
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")



    @pytest.mark.parametrize('language', ["ru", "en-gb"])  # Параметризация
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")




# pytest -s -v test_fixture1.py

# pytest -s -v -m smoke test_fixture1.py    - запуск теста с маркировкой smoke
# pytest -s -v -m "not smoke" test_fixture1.py  - запуск всех кроме smoke
# pytest -s -v -m "smoke or regression" test_fixture1.py
# pytest -s -v -m "smoke and win10" test_fixture1.py  - запустить только smoke скоторые с  Win10
# pytest -rx -v test_fixture1.py  - сообщение в консоли об пропуске бага о котором знаем