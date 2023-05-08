import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):

    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")