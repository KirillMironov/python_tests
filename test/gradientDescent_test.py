import test.gradientDescent as gd
import math
import unittest
from scipy.misc import derivative


class DerivativeTest(unittest.TestCase):

    def f(self, x):
        return 2*x**2

    def test_derivative(self):
        self.assertAlmostEqual(4.0, derivative(self.f, 1.0), places=5)
        self.assertAlmostEqual(13.2, derivative(self.f, 3.3), places=5)

    def test(self):
        epsilon = 0.01
        min_step = 0.0000001

        self.assertAlmostEqual(0.9999951805, gd.calculate(lambda x: 2 * (x - 1), 0.0, epsilon, min_step), places=5)
        #self.assertAlmostEqual(math.pi+1, gd.calculate(lambda x: x**3-3*x**2+2*x, 1.0, epsilon, min_step), places=5)
        self.assertAlmostEqual(4.71236198, gd.calculate(lambda x: math.exp(math.sin(x))*math.cos(x), 2.0, epsilon, min_step), places=5)


if __name__ == '__main__':
    unittest.main()
