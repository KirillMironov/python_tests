import unittest
import numpy as np


class MatrixTest(unittest.TestCase):

    def test_matrix(self):
        matrix = np.array([[1, 2], [2, 3]])
        self.assertTrue(matrix, )

if __name__ == '__main__':
    unittest.main()
