import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(autouse=True)
def web_browser():
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options
    # browser.config.window_width = 1400
    # browser.config.window_height = 1600
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1%1234@selenoid:autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()
