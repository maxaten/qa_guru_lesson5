import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser.config.driver_options = chrome_options
    # browser.config.driver_name = 'chrome'
    browser.driver.set_window_size(1920, 1080)
    # browser.driver.execute_script("document.body.style.zoom='70%'")
    # browser.execute_script('document.querySelector("footer","#fixedban").remove();')
    # browser.config.window_width = 1920
    # browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'