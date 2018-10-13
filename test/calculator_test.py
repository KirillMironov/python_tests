import test.calculator as c
import unittest


class CalculatorTest(unittest.TestCase):

    def test_calculate(self):
        c.hello()
        calc = c.Calculator
        self.assertEqual(4, calc.calculate(2, 2))


if __name__ == '__main__':
    unittest.main()
