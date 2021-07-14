import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Non_Commerce.TestData.Login_Data import TestLogin_Data
from Non_Commerce.utilities.BaseClass import BaseClass


class LoginPage(BaseClass):
    base = BaseClass()
    log = base.get_logger()

    def __init__(self, driver):
        self.driver = driver


    def getUserName(self, getLoginData):
        UserName = (By.ID, 'Email')
        LoginPage.log.info("Entering First Name as " + getLoginData["UserName"])
        return self.driver.find_element(*UserName)

    def getPassword(self, getLoginData):
        Password = (By.ID, "Password")
        LoginPage.log.info("Entering Password  as " + getLoginData["Password"])
        return self.driver.find_element(*Password)

    def getLoginBTN(self):
        SubmitBtn = (By.XPATH, "//button[@type='submit']")
        time.sleep(3)
        LoginPage.log.info("Clicking on Login Button")

        return self.driver.find_element(*SubmitBtn)

    def clearText(self, locator):
        cleartext = (By.ID, locator)
        return self.driver.find_element(*cleartext)

    def logout(self):
        louout = (By.LINK_TEXT, 'Logout')
        time.sleep(3)
        LoginPage.log.info("Clicking on Logout Button")
        return self.driver.find_element(*louout)

    def verifyHomePageTitle(self, config, getLoginData):

        try:
            Actualtitile = self.driver.title
            assert getLoginData[config] == Actualtitile
            LoginPage.log.info("Verify Home page Title  as " + getLoginData[config])
        except AssertionError  as e:
            self.driver.save_screenshot(".\\screenshot\\"+"homepage.png")
            LoginPage.log.error("Verify both value are  wrong "+format(e))

        #if Actualtitile == getLoginData[config]:
            #assert True
            #LoginPage.log.info("Verify Home page Title  as " + getLoginData[config])
        #else:
            #LoginPage.log.error("failed Home page Title ")
            #assert False

    def get_boolean(self, config, getLoginData):
        self.getLoginData = getLoginData
        if bool(getLoginData[config]) == True:
            return True
        else:
            return False

    def getLoginAction(self, getLoginData):
        # log= LoginPage(self.driver)
        # we also use this type but if we use this type than every method attached this log,
        # so dont pass self parametes bcoz you already pass self as object
        log = LoginPage

        if log.get_boolean(self, 'ConfigUserName', getLoginData):  # LoginPage.get_boolean(log)
            log.clearText(self, 'Email').clear()
            log.getUserName(self, getLoginData).send_keys(getLoginData["UserName"])

        if log.get_boolean(self, 'ConfigUserPassword', getLoginData):
            log.clearText(self, 'Password').clear()
            log.getPassword(self, getLoginData).send_keys(getLoginData["Password"])

        if log.get_boolean(self, 'ConfigLoginButton', getLoginData):
            log.getLoginBTN(self).click()
            time.sleep(5)

        if log.get_boolean(self, 'ConfigTraverseHomePage', getLoginData):
            log.verifyHomePageTitle(self, 'TraverseHomePage', getLoginData)

        #if log.get_boolean(self, 'ConfigLogoutButton', getLoginData):
         #   log.logout(self).click()
          #  time.sleep(5)











    @pytest.fixture(params=TestLogin_Data.getLogin_Data())
    def getLoginData(self, request):
        return request.param