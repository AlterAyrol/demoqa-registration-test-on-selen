from selene import browser
import os


def send_picture(locator):
    browser.element(locator).send_keys(os.path.join(os.path.dirname(__file__), 'for_send.bmp'))
