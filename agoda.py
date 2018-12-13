# -*- coding: utf-8 -*-
import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?city=5085&checkIn=2018-12-27&los=1&rooms=1&adults=2&children=0&languageId=20&userId=69706359-fe0e-4772-8f1c-743729fcf4ad&sessionId=ekyozcvsik30dpm2db1njfys&pageTypeId=1&origin=TW&locale=zh-TW&cid=-999&aid=178961&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=69706359-fe0e-4772-8f1c-743729fcf4ad&prid=0&checkOut=2018-12-28&priceCur=TWD&textToSearch=%E6%9D%B1%E4%BA%AC&travellerType=1&productType=-1&sort=agodaRecommended")
suop = BeautifulSoup(browser.page_source)
browser.find_element_by_id("paginationNext").click()
browser.close()


'''
driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
'''