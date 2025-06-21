import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Interface language (e.g., en, fr, ru)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    browser = None
    try:
        if browser_name == "chrome":
            options = Options()
            options.add_experimental_option(
                "prefs", {"intl.accept_languages": user_language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name must be 'chrome' or 'firefox'")

        yield browser
    finally:
        if browser is not None:
            browser.quit()