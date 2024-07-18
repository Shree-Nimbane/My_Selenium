import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData  ## impoting classes from our projet folders
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):      ## inheritance
    '''
        TestHomePage => Child class
        BaseClass => Parent class
        inheritance # we are inheriting BaseClass into TestHomePage
        So all the properties of base class will be available to child
        All properties or methods will be inherited in child
    '''

    def test_formSubmission(self,getData):
        time.sleep(5)
        log = self.getLogger()      ## creating logger object to maintain or write logs
        ## self.driver we will get from setup fixture which is been used by parent BaseClass
        homepage= HomePage(self.driver)     ## Creating object of HomePage and passing driver in parameterized contructor
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getpass().send_keys(getData["password"])
        time.sleep(5)
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        homepage.getEmpStats().click()
        homepage.getStudentStat().click()
        homepage.submitForm().click()
        homepage.getclander().send_keys(getData['date'])
        time.sleep(5)

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[{"firstname": "Sagar", "lastname":"Sarade",'date':'07-10-1997', "Gender": "Male","password":"123457"}, {"firstname": "Yusuf", "lastname":"Tamboli", "Gender": "Male","password":"123456",'date':'07-10-1997'}])
    ###@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):     #request is default object of fixture which automatically initilized when fixture is being executed
        return request.param


