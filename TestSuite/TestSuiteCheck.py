'''
Created on May 24, 2017

@author: tarun.walia
'''
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from FirstTest.FirstTest import TestGoogleSearch
from ReportTestRunner import HTMLTestRunner 

reportDir= "D:\JavaWorkspace\PythonSelenium\Reports"
os.path.abspath(reportDir)

search_text = unittest.TestLoader().loadTestsFromTestCase(TestGoogleSearch)

test_suite = unittest.TestSuite([search_text])
outputFile = open(reportDir+"\Report.html","w")

runner = HTMLTestRunner.HTMLTestRunner(stream=outputFile,title='Test Report', description='Python Test Tarun')


runner.run(test_suite)