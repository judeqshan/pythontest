# -*- coding: UTF-8 -*-
 
import unittest
from test_mathfunc import TestMathFunc
# from facade.HTMLTestRunner import HTMLTestRunner
 
if __name__ == '__main__':
    suite = unittest.TestSuite()
 
   
    
    # use TestLoader to get TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
 
    #generate txt format report    
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
 
    # with open('HTMLReport.html','w') as f:
    #     runner = HTMLTestRunner(stream = f,
    #                             title = u'test report',
    #                             description = u'test results',
    #                             verbosity = 2
    #                             )
    #     runner.run(suite)