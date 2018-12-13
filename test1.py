# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?city=5085&checkIn=2018-12-27&los=1&rooms=1&adults=2&children=0&languageId=20&userId=69706359-fe0e-4772-8f1c-743729fcf4ad&sessionId=ekyozcvsik30dpm2db1njfys&pageTypeId=1&origin=TW&locale=zh-TW&cid=-999&aid=178961&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=69706359-fe0e-4772-8f1c-743729fcf4ad&prid=0&checkOut=2018-12-28&priceCur=TWD&textToSearch=%E6%9D%B1%E4%BA%AC&travellerType=1&productType=-1&sort=agodaRecommended")
        driver.find_element_by_id("paginationNext").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
