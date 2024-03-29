import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, ru, by, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    chrome_path = r"/usr/local/bin/chromedriver"
    firefox_path = Service(r"/usr/local/bin/geckodriver")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = Chrome_Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(chrome_path, options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_ff = FF_Options()
        options_ff.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(service=firefox_path, options=options_ff)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
