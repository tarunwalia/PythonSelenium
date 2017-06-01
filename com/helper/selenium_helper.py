'''
Created on May 22, 2017

@author: tarun.walia
'''

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
class SeleniumHelper():
    
  
    def initializeWebdriver(self, driverType):
        if(driverType == 'Firefox'):            
            binary = FirefoxBinary("D:/JavaWorkspace/PythonSelenium/geckodriver/geckodriver/geckodriver.exe")
            self.driver  =webdriver.Firefox(firefox_binary=binary)
            
        elif driverType =='Chrome':
            self.driver = webdriver.Chrome(executable_path='D:\JavaWorkspace\PythonSelenium\chrome\chromedriver.exe')
        else:
            raise Exception ("Unknown browser.")  
      
    def navigateToUrl(self, url):
        try:
            self.driver.get(url)  
        except:
            raise Exception("URL Unknown")   
        
    def closeBrowser(self):
        try:
            self.driver.close()
        except:
            raise Exception("browser not close")             
        
        
    def searchString(self, searchString):
        try:
            input=self.driver.find_elements_by_xpath('//input[@type="text" and @name="q"]')[0]
            if not input.is_displayed():
                raise Exception("input field is not displayed")
            input.clear()
            input.send_keys(searchString+Keys.RETURN)      
        except:
            raise Exception("No input field")   
        
    
    def checkSearchBox(self):
        valueC = self.driver.find_element_by_name('btnK').get_attribute("name");
        print valueC
        return valueC
        
        
        
        