import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_buy_button_exist(browser):
    browser.get(link)

    time.sleep(5)

    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    assert button.is_displayed(), "Button is not displayed!"
    assert button.is_enabled(), "Button is not enabled!"