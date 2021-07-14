import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Non_Commerce.TestData.Product_Catalog import TestProduct_Catalog

from Non_Commerce.utilities.BaseClass import BaseClass


class CatalogPage(BaseClass):
    base = BaseClass()
    log = base.get_logger()

    def __init__(self, driver):
        self.driver = driver

    def ClickCatalog(self):
        CatalogBtn = (By.LINK_TEXT, "Catalog")
        time.sleep(3)
        CatalogPage.log.info("Clicking on Catalog Button")

        return self.driver.find_element(*CatalogBtn)

    def Clickproduct(self):
        productBtn = (By.XPATH, "//li[@class='nav-item has-treeview menu-open']//p[text()=' Products']")
        time.sleep(3)
        CatalogPage.log.info("Clicking on Product Button")

        return self.driver.find_element(*productBtn)

    def ClickAddNewproduct(self):
        addproductBtn = (By.XPATH, "//a[@class='btn btn-primary']")
        time.sleep(3)
        CatalogPage.log.info("Clicking on Add New Product Button")

        return self.driver.find_element(*addproductBtn)

    def ClickOnProdctInfo(self):
        #addproductBtn = (By.XPATH, "//div[@class='card-title'][contains(text(),'Product info')]")
        productname=self.driver.find_element_by_xpath("//label[contains(text(),'Product name')]").is_displayed()
        #sss = productname.is_displayed()
        if bool(productname) == True:
            CatalogPage.log.info("Clicking on Product Info Button")
        else:
            addproductBtn = self.driver.find_element_by_xpath("(//div[contains(text(),'Product info')])[1]")
            self.driver.execute_script("arguments[0].click();", addproductBtn)
            time.sleep(3)
            CatalogPage.log.info("Clicking on Product Info Button")

        #return self.driver.find_element(*addproductBtn)
        #return self.driver.execute_script("arguments[0].click();", addproductBtn)

    def EnterproductName(self):
        addproductBtn = (By.XPATH, "//input[@id='Name']")
        time.sleep(3)
        CatalogPage.log.info("Enter Product Name")

        return self.driver.find_element(*addproductBtn)

    def EnterShortDescriptio(self):
        addproductBtn = (By.XPATH, "//textarea[@id='ShortDescription']")
        time.sleep(3)
        CatalogPage.log.info("Enter Short Description")

        return self.driver.find_element(*addproductBtn)

    def EnterSKU(self):
        addproductBtn = (By.XPATH, "//input[@id='Sku']")
        time.sleep(3)
        CatalogPage.log.info("Enter SKU")

        return self.driver.find_element(*addproductBtn)

    def select_value_multi(self,option_list,val):
        for ele in option_list:
            li=[]
            li.append(val)
            for k in range(len(li)):
                if ele.text == li[k]:
                    ele.click()
                    break


        time.sleep(3)




    def SelectCategories(self,getCatalogData):
        self.driver.find_element_by_xpath("(//div[@class='k-multiselect-wrap k-floatwrap'])[1]").click()
        time.sleep(3)
        #sss=self.driver.find_elements_by_css_selector("ul#SelectedCategoryIds_listbox li")
        option_list = self.driver.find_elements_by_xpath("//ul[@id='SelectedCategoryIds_listbox']//li")
        val=getCatalogData['Categories']
        self.select_value_multi(option_list,val)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()
        CatalogPage.log.info("Select Catagoris")

    def SelectManufacturers(self,getCatalogData):
        self.driver.find_element_by_xpath("(//div[@class='k-multiselect-wrap k-floatwrap'])[2]").click()
        time.sleep(3)
        #sss=self.driver.find_elements_by_css_selector("ul#SelectedCategoryIds_listbox li")
        option_list = self.driver.find_elements_by_xpath("//ul[@id='SelectedManufacturerIds_listbox']//li")
        val = getCatalogData['Manufacturer']
        self.select_value_multi(option_list, val)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()

        CatalogPage.log.info("Select Manufacture")

    def SelectChecked(self,getCatalogData):
        result = self.driver.find_element_by_xpath("//input[@id='Published']").is_selected()
        if result:
            CatalogPage.log.info("Checkbox already selected")
        else:
            if getCatalogData['Publish'] == 'Check':
                self.driver.find_element_by_xpath("//input[@id='Published']").click()
                CatalogPage.log.info('Checkbox selected')
            else:
                CatalogPage.log.info("Checkbox does not  selected")

    def month_select(self,sp):
        months = self.driver.find_elements_by_xpath("//table[@role='grid']//tr//a")
        Month_List = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for month in months:
            mn = month.text
            num = sp[1]
            conv_int = int(num)
            Get_Month = Month_List[conv_int - 1]
            if mn == Get_Month:
                month.click()
                break

    def selectSatrtdate(self,date):

        self.driver.find_element_by_xpath("(//span[@class='k-icon k-i-calendar'])[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").click()
        time.sleep(2)
        year = self.driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").text
        sp = date.split("/")
        yy = sp[2]
        if yy == year:
            self.month_select(sp)

        else:
            while yy < year:
                self.driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[1]").click()
                year = self.driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").text
            while yy > year:
                self.driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[3]").click()
                year = self.driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").text
            self.month_select(sp)

        dates = self.driver.find_elements_by_xpath("//table[@class='k-content k-month']//a")
        for dd in dates:
            dates = dd.text
            if dates == sp[0]:
                dd.click()
                break

    def selectEnddate(self,date):

        self.driver.find_element_by_xpath("(//span[@class='k-icon k-i-calendar'])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//div[@id='AvailableEndDateTimeUtc_dateview']//a)[2]").click()
        year = self.driver.find_element_by_xpath("(//div[@id='AvailableEndDateTimeUtc_dateview']//a)[2]").text
        sp = date.split("/")
        yy = sp[2]
        if yy == year:
            self.month_select(sp)

        else:
            while yy < year:
                self.driver.find_element_by_xpath("(//div[@id='AvailableEndDateTimeUtc_dateview']//a)[1]").click()
                year = self.driver.find_element_by_xpath("(//div[@id='AvailableEndDateTimeUtc_dateview']//a)[2]").text
            while yy > year:
                self.driver.find_element_by_xpath("(//div[@id='AvailableEndDateTimeUtc_dateview']//a)[3]").click()
                year = self.driver.find_element_by_xpath("(//div[@id='AvailableEndDateTimeUtc_dateview']//a)[2]").text
            self.month_select(sp)

        dates = self.driver.find_elements_by_xpath("(//table[@role='grid'])[2]//a")
        for dd in dates:
            dates = dd.text
            if dates == sp[0]:
                dd.click()
                break

    def AvailableStartDate(self,getCatalogData):

        self.selectSatrtdate(getCatalogData['AvailableStartDate'])

        CatalogPage.log.info("Select Available Start Date")

    def AvailableEndDate(self,getCatalogData):

        self.selectEnddate(getCatalogData['AvailableEndDate'])

        CatalogPage.log.info("Select Available END Date")

    def Save(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@name='save']").click()

        CatalogPage.log.info("Click on Save Button")

    def get_boolean(self, config, getCatalogData):
        self.getCatalogData = getCatalogData
        if bool(getCatalogData[config]) == True:
            return True
        else:
            return False

    def getCatalogAction(self, getCatalogData):
        log = CatalogPage

        if log.get_boolean(self, 'ConfigCatalog', getCatalogData):
            log.ClickCatalog(self).click()

        if log.get_boolean(self, 'ConfigProduct', getCatalogData):
            log.Clickproduct(self).click()

        if log.get_boolean(self, 'ConfigAddNewButton', getCatalogData):
            log.ClickAddNewproduct(self).click()

        if log.get_boolean(self, 'configProductInfo', getCatalogData):
            log.ClickOnProdctInfo(self)

        if log.get_boolean(self, 'ConfigProductName', getCatalogData):
            log.EnterproductName(self).send_keys(getCatalogData["ProductName"])

        if log.get_boolean(self, 'ConfigShortDescription', getCatalogData):
            log.EnterShortDescriptio(self).send_keys(getCatalogData["ShortDescription"])

        if log.get_boolean(self, 'ConfigSKU', getCatalogData):
            log.EnterSKU(self).send_keys(getCatalogData["SKU"])

        if log.get_boolean(self, 'ConfigCategories', getCatalogData):
            log.SelectCategories(self,getCatalogData)

        if log.get_boolean(self, 'ConfigManufectres', getCatalogData):
            log.SelectManufacturers(self,getCatalogData)

        if log.get_boolean(self, 'ConfigPublish', getCatalogData):
            log.SelectChecked(self,getCatalogData)

        read_more = self.driver.find_element_by_xpath("//label[contains(text(),'Require other products') and @for='RequireOtherProducts']")
        self.driver.execute_script("arguments[0].scrollIntoView();", read_more)


        if log.get_boolean(self, 'ConfigAvailableStartDate', getCatalogData):
            log.AvailableStartDate(self,getCatalogData)

        if log.get_boolean(self, 'ConfigAvailableEndDate', getCatalogData):
            log.AvailableEndDate(self,getCatalogData)

        read_more = self.driver.find_element_by_xpath("//form[@id='product-form']//h1")
        self.driver.execute_script("arguments[0].scrollIntoView();", read_more)

        if log.get_boolean(self, 'ConfigSave', getCatalogData):
            log.Save(self)




    @pytest.fixture(params=TestProduct_Catalog.getProduct_Catalog())
    def getCatalogData(self, request):
        return request.param