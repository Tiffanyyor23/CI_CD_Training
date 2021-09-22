#!/usr/bin/env python3

import unittest 
from calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):

    def test_Calculator(self):
        answer = Calculator(1,8)        
        self.assertEqual(answer, int(9))

if __name__ == "__main__":
    unittest.main()
