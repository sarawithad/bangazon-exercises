import unittest
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
    # Create an instance of the calculator that can be used in all tests

    @classmethod
    def tearDownClass(self):
        print('Tear down class')


    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2,2), 4)

    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2,2), 0)

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2,3), 6)

    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10,5), 2)



if __name__ == '__main__':
    unittest.main()

