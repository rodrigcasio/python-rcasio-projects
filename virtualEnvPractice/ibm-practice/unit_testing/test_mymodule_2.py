"""
Improved test script
Testing within a class, each function in a test_(name) function from the 'TestMyModule" class
"""

import unittest 
from mymodule import square, double, add

class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_double(self):
        self.assertEqual(double(0), 0)
    
    def test_add(self):
        self.assertEqual(add(5, 5), 10)
        self.assertNotEqual(add(9, 10), 21)

if __name__ == "__main__":
    unittest.main()
