import unittest
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    # Create an instance of the calculator that can be used in all tests

    @classmethod
    def tearDownClass(self):
        print('Tear down class')


    def test_add(self):
        # calculator = Calculator() --dont need bc setUpClass^^
        self.assertEqual(self.calculator.add(2,2), 4)

    def test_subtract(self):
        # calculator = Calculator()
        self.assertEqual(self.calculator.subtract(2,2), 0)

    def test_multiply(self):
        # calculator = Calculator()
        self.assertEqual(self.calculator.multiply(2,3), 6)

    def test_divide(self):
        # calculator = Calculator()
        self.assertEqual(self.calculator.divide(10,5), 2)


if __name__ == '__main__':
    unittest.main()


# test ran on command line: python CalcTest.py -v
#no need to use discover command b/c only one test module in this directory


