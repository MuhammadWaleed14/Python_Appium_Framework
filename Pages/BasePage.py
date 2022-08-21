import logging
from appium.webdriver.common.appiumby import AppiumBy
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_type, locator):
        try:
            if str(locator_type).upper() == "XPATH":
                self.driver.find_element(by=AppiumBy.XPATH, value=locator).click()
            elif str(locator_type).upper() == "ACCESSIBILITYID":
                self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=locator).click()
            elif str(locator_type).upper() == "ID":
                self.driver.find_element(by=AppiumBy.ID, value=locator).click()
            log.logger.info("Clicking on an Element " + str(locator))
        except Exception as e:
            log.logger.error("Exception occurred during web-element click " + str(locator))
            print("Exception occurred during web-element click" + str(repr(e)))

    def type(self, locator_type, locator, value):
        try:
            if str(locator_type).upper() == "XPATH":
                self.driver.find_element(by=AppiumBy.XPATH, value=locator).send_keys(value)
            elif str(locator_type).upper() == "ACCESSIBILITYID":
                self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=locator).send_keys(value)
            elif str(locator_type).upper() == "ID":
                self.driver.find_element(by=AppiumBy.ID, value=locator).send_keys(value)
            log.logger.info("Typing in an Element " + str(locator) + " entered the value as : " + str(value))
        except Exception as e:
            log.logger.error("Exception occurred during typing in an Element " + str(locator) + " entered the value as : " + str(value))
            print("Exception occurred during web-element type" + str(repr(e)))

    def getText(self, locator_type, locator):
        try:
            if str(locator_type).upper() == "XPATH":
                text = self.driver.find_element(by=AppiumBy.XPATH, value=locator).text
            elif str(locator_type).upper() == "ACCESSIBILITYID":
                text = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=locator).text
            elif str(locator_type).upper() == "ID":
                text = self.driver.find_element(by=AppiumBy.ID, value=locator).text
            log.logger.info("Get Element Text" + str(locator))
            return text
        except Exception as e:
            log.logger.error("Exception occurred during get web-element text" + str(locator))
            print("Exception occurred during get web-element text" + str(repr(e)))

    def isDisplayed(self, locator_type, locator):
        try:
            if str(locator_type).upper() == "XPATH":
                assert self.driver.find_element(by=AppiumBy.XPATH, value=locator).is_displayed()
            elif str(locator_type).upper() == "ACCESSIBILITYID":
                assert self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=locator).is_displayed()
            elif str(locator_type).upper() == "ID":
                assert self.driver.find_element(by=AppiumBy.ID, value=locator).is_displayed()
            log.logger.info("Element is Displayed " + str(locator))
        except Exception as e:
            log.logger.error("Exception occurred during web-element display verification" + str(locator))
            print("Exception occurred during web-element display verification" + str(repr(e)))
