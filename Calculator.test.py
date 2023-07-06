import unittest

from Calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
      self.calculator =Calculator()

    def test_add(self):
        result = self.calculator.add(20, 4)
        self.assertEqual(result, 24)

    def test_sub(self):
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result,5)

    def test_mult(self):
        result = self.calculator.muliply(2, 3)
        self.assertEqual(result, 6)

    def test_devide(self):
        result = self.calculator.devide(4, 2)
        self.assertEqual(result, 2)

    def test_sqrt(self):
        result = self.calculator.square_root(4)
        self.assertEqual(result, 2)

    def test_expo(self):
        result = self.calculator.exponent(4, 2)
        self.assertEqual(result, 16)



if __name__ == '__main__':
            unittest.main()
