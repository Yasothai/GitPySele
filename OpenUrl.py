#Yaso
import unittest
from selenium import webdriver

driver = webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://google.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.close()
driver.quit()
