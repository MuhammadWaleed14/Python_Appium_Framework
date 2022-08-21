from pathlib import Path
import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['app'] = str(Path().absolute().parent) + '/App/app-debug.apk'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
