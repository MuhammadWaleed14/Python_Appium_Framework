from Pages.BasePage import BasePage
from Utilities.Locators import Locators


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password):
        self.type("ID", Locators.username_ID, username)
        self.type("ID", Locators.password_ID, password)
        self.click("ID", Locators.signbtn_ID)

    def verify_login_successfully(self):
        self.isDisplayed("ACCESSIBILITYID", Locators.homeicon_ACCESSIBILITYID)
