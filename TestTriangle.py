# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 1), "Isoceles", '1, 2, 1 should be isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene', '1,2,3 should be scalene')
    
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(300, 3, 42), 'InvalidInput', 'input over 200 is invalid')
        self.assertEqual(classifyTriangle(-1, -3, 0), 'InvalidInput', 'input less than 1 should be invalid')
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', "input less than 1 should be invalid")
        self.assertEqual(classifyTriangle(3,4,10), "InvalidInput", 'not valid triangles should not be valid')
        self.assertEqual(classifyTriangle("hi", "hi",2), 'InvalidInput', 'string input should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

