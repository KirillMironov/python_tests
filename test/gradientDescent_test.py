import test.gradientDescent as gd
import math
import unittest


def test(self):
    epsilon = 0.01
    minStep = 0.0000001
    delta = 0.00001

    self.assertEquals(1.0, gd.calculate(lambda x: 2 * (x - 1), 0.0, epsilon, minStep), delta)
    self.assertEquals(math.pi+1, gd.calculate(lambda x: math.sin(x-1), 2.0, epsilon, minStep), delta)
    self.assertEquals(4.7123889, gd.calculate(lambda x: math.exp(math.sin(x))*math.cos(x), 2.0, epsilon, minStep), delta)


if __name__ == '__main__':
    unittest.main()
