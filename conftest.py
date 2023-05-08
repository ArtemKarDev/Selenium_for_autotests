
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session") # декаратор с помощью которого последующая функция с конфигами распространяется на сессию
def browser():
    """
    Main fixture
    """
    print("\nstart browser for test..")
    # Опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")     # открываем на полный экран
    chrome_options.add_argument("--disable-infobars")  # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions")     # отключаем расширения
    chrome_options.add_argument("--disable-gpu")  # применять только программные средства ОС
    chrome_options.add_argument("--disable-dev-shm-usage")  #  преодолеть проблемы с ограниченными ресурсами
    # chrome_options.add_argument("--headless")     # спец режим "без окна браузера"

    # with open("logfile.txt", "w", encoding="utf-8") as f: #лог файл будет создан в той же директории
    #     f.write("")

    # устанавливаем webdrive в соответсвии с версией используемого браузера
    # https://github.com/SergeyPirogov/webdriver_manager/blob/master/README.md
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver    # в случае падения теста принудительно закрывает окна браузера
    print("\nquit browser..")
    driver.quit()


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