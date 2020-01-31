from selenium import webdriver
import unittest
#from selenium.webdriver.commeon.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('gmail.com')

    def test_01(self):
        driver = self.driver
        input_login = driver.find_element_by_id('identifierId')
        input_login.send_keys('TestingSMUser@gmail.com')


if __name__ == "__main__":
    unittest.main()
