'''
Created on May 19, 2017

@author: tarun.walia
'''
import unittest
from selenium import webdriver
from com.helper.selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from distutils.log import set_verbosity

class TestGoogleSearch(unittest.TestCase):  
    
        
    def test_searchField(self):        
        seleniumHelperInt.initializeWebdriver("Chrome")
        seleniumHelperInt.navigateToUrl("http://www.google.com")
        seleniumHelperInt.searchString("tarun walia")
        seleniumHelperInt.closeBrowser()
    
    def test_checkSearchBox(self):  
        seleniumHelperInt.initializeWebdriver("Chrome")
        seleniumHelperInt.navigateToUrl("http://www.google.com") 
        self.assertEqual(seleniumHelperInt.checkSearchBox(), 'btnK',"Name is not matching.")
        
    #def test_checkLanguage(self):
       # self.assertTrue(self.is_element_present(self,By.ID), "_eEe")  
        
        
    def is_element_present(self, how, what):    
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException,e: return False  
        return True  
    
seleniumHelperInt = SeleniumHelper()   

if __name__ == '__main__':
       # seleniumHelperInt = SeleniumHelper()
        unittest.main(verbosity=2)
