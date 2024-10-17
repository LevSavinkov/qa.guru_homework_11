import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from src.utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = "https://demoqa.com/"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    options.page_load_strategy = "eager"
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    
    browser.config.driver = driver
    
    yield browser
    
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    
    browser.quit()
