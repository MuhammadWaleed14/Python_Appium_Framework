from Test.BaseTest import BaseTest
from Pages.Login import Login
from TestData.LoginData import LoginData


class Test_Login(BaseTest):

    def __int__(self):
        self.loginPage = Login(self.driver)

    def test_login(self):
        self.loginPage = Login(self.driver)
        self.loginPage.do_login(LoginData.USERNAME, LoginData.PASSWORD)
        self.loginPage.verify_login_successfully()
