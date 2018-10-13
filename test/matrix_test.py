import unittest
import numpy as np


class MatrixTest(unittest.TestCase):

    def test_matrix(self):
        matrix1 = np.array([[-1, 1], [2, 0], [0, 3]])
        matrix2 = np.array([[3, 1, 2], [0, -1, 4]])
        result = matrix1 @ matrix2
        np.testing.assert_array_equal(result, [[-3, -2, 2], [6, 2, 4], [0, -3, 12]])


if __name__ == '__main__':
    unittest.main()
