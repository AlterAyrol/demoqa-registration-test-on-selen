import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def web_browser():
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
