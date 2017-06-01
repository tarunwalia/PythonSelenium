'''
Created on May 23, 2017

@author: tarun.walia
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import FirstTest



search_text = unittest.TestLoader().loadTestsFromTestCase(FirstTest.FirstTest.TestGoogleSearch)

test_suite = unittest.TestSuite([search_text])

unittest.TextTestRunner(verbosity=2).run(test_suite)