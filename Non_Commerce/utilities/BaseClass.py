import inspect
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
#from TCS.TestData.DashboardEntity_Data import Dashboard_Data

from Non_Commerce.TestSuites.Test_Scenarion_Data import Test_Scenario_Data
from datetime import datetime
import os

from Non_Commerce.TestData.Login_Data import TestLogin_Data


@pytest.mark.usefixtures("setup")
class BaseClass:


    def getTestDataAddress(self,Product):
        if Product == "PL" :
            PL_Testdata_address = "D://ABFL_Python_TestData//TestData//PL//WebAutomationTestData.xlsx"
            return PL_Testdata_address
        else:
            LAP_Testdata_address = "D://ABFL_Python_TestData//TestData//LAP//WebAutomationTestDataLAP.xlsx"
            return LAP_Testdata_address


    def getTestSuiteAddress(self,Product):
        if Product == "PL" :
            PL_TestSuite_address = "D://ABFL_Python_TestData//TestSuites//1000_TestScenarios_PLTestSuite.xlsx"
            return PL_TestSuite_address
        else:
            LAP_TestSuite_address = "D://ABFL_Python_TestData//TestSuites//1000_TestScenarios_LAPTestSuite.xlsx"
            return LAP_TestSuite_address

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def WebDriverWait(self, Xpath):
        wait = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.XPATH, Xpath)))


    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        if not os.path.exists('D://PycharmProjects//MyThird_Project//LOG_REPORT'):
            os.makedirs('D://PycharmProjects//MyThird_Project//LOG_REPORT')

        TestScanerio_Obj = str(Test_Scenario_Data.getscenario()['TestCase'])
        date_TestCase = datetime.now().strftime("%d-%m-%Y %I-%M-%S %p")+" " + TestScanerio_Obj
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("D://PycharmProjects//MyThird_Project//LOG_REPORT//"+date_TestCase)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger


    def get_boolean(self, config, getLoginData):
        self.getLoginData = getLoginData
        if bool(getLoginData[config]) == True:
            return config
        else:
            return False

    def get_boolean1(self, config, getDashboardEntityData):
        self.getDashboardEntityData = getDashboardEntityData
        if bool(getDashboardEntityData[config]) == True:
            return config
        else:
            return False

    def get_WebdriverWait(self, locator):
        WebDriverWait(self.driver, 28).until(EC.element_to_be_clickable((locator)))

    def get_WebdriverWait_Cibil_sample(self, locator):
        WebDriverWait(self.driver, 58).until(EC.element_to_be_clickable((locator)))

    def get_PageBottom_Scroll(self):
        sample = self.driver.find_element_by_tag_name("html")
        return sample.send_keys(Keys.END)

    def get_WebdriverWaitClick_Xpath_String( self, locator ):
        element = WebDriverWait(self.driver, 28).until(EC.element_to_be_clickable((By.XPATH,locator)))
        return  element.click()

    def getSendKeys(self,locator,value):
        element = WebDriverWait(self.driver, 28).until(EC.element_to_be_clickable((By.XPATH,locator)))
        element.clear()
        return  element.send_keys(value)

    def getSendKeysID(self,locator,value):
        element = WebDriverWait(self.driver, 28).until(EC.element_to_be_clickable((By.ID,locator)))
        element.clear()
        return  element.send_keys(value)

    def get_PageDown(self,locator,time):
        for x in range(0,time):
            self.driver.find_element_by_xpath(locator).send_keys(Keys.PAGE_DOWN)
            #driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)


    def get_Keyboard_Key(self,Key):
        act = ActionChains(self.driver)
        act.send_keys(Key).perform()



    #@pytest.fixture(params=TestLogin_Data.getLogin_Data())
    #def getLoginData(self, request):
         #return request.param


    #@pytest.fixture(params=Dashboard_Data.getDashboardEntity_Data())
    #def getDashboardEntityData( self, request ):
        #return request.param

    # @pytest.fixture(params=Dashboard_Data.getDashboardEntity_Data())
    # def getDashboardEntity_Data(self, request):
    #     return request.param

