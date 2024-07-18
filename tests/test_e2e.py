import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        time.sleep(5)
        cards = checkoutpage.getCardTitles()
        # time.sleep(5)
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        time.sleep(5)
        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        # self.driver.find_element_by_id("country").send_keys("ind")
        self.driver.find_element(By.ID,"country").send_keys('ind')
        # # time.sleep(5)
        self.verifyLinkPresence("India")
        #
        # self.driver.find_element_by_link_text("India").click()
        self.driver.find_element(By.LINK_TEXT,"India").click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

        # self.driver.find_element_by_css_selector("[type='submit']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        # textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)
        #
        assert ("Success! Thank you!" in textMatch)
