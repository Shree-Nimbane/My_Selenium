from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    '''
        POM  => Page object model

    '''
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    __name = (By.CSS_SELECTOR, "[name='name']")
    __email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    Pass=(By.XPATH,'//*[@id="exampleInputPassword1"]')
    StudentStat=(By.XPATH,'//*[@id="inlineRadio1"]')
    EmployedStat=(By.XPATH,'//*[@id="inlineRadio2"]')
    clander=(By.XPATH,'/html/body/app-root/form-comp/div/form/div[7]/input')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.__name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.__email)    # * is used to unpack tuple in parameters
        ## HomePage.email[0], HomePage.email[1] => *HomePage.email


    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

    def getpass(self):
        return self.driver.find_element(*HomePage.Pass)


    def getEmpStats(self):
        return self.driver.find_element(*HomePage.EmployedStat)


    def getStudentStat(self):
        return self.driver.find_element(*HomePage.StudentStat)



    def getclander(self):
        return self.driver.find_element(*HomePage.clander)



