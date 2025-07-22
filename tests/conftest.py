import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()