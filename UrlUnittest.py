import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.driver = webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver.exe")
        self.driver.set_page_load_timeout(20)
        self.driver.get("http://google.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.assertEqual(self.driver.title,'Google','Failed' )


if __name__ == '__main__':
    unittest.main()
