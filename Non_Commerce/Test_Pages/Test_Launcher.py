import pytest

from Non_Commerce.Page_Object.CatalogPage import CatalogPage
from Non_Commerce.Page_Object.LoginPage import LoginPage
from Non_Commerce.TestData.Login_Data import TestLogin_Data
from Non_Commerce.TestData.Product_Catalog import TestProduct_Catalog
from Non_Commerce.utilities.BaseClass import BaseClass


class Test_Launcher(BaseClass):
    base = BaseClass()

    log = base.get_logger()

    @pytest.mark.run(order=1)
    def test_LoginPage(self, getLoginData):
        loginPage = LoginPage(self.driver)
        loginPage.getLoginAction(getLoginData)

    @pytest.mark.run(order=2)
    def test_CatalogPage(self, getCatalogData):
       catalogpage = CatalogPage(self.driver)
       catalogpage.getCatalogAction(getCatalogData)



    @pytest.fixture(params=TestLogin_Data.getLogin_Data())
    def getLoginData(self, request):
        return request.param

    @pytest.fixture(params=TestProduct_Catalog.getProduct_Catalog())
    def getCatalogData(self, request):
        return request.param