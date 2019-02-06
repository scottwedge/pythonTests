from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://gmail.com')

    def test_01(self):
        driver = self.driver
        input_login = driver.find_element_by_id('identifierId')
        input_login.send_keys('TestingSMUser@gmail.com')

        next_button_one = driver.find_element_by_class_name('CwaK9')
        next_button_one.click()

        input_passwrod = driver.find_element_by_class_name('whsOnd zHQkBf')
        next_button_two.click()




if __name__ == '__main__':
    unittest.main()
