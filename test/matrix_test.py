import unittest
import numpy as np


class MatrixTest(unittest.TestCase):

    def test_matrix(self):
        matrix = np.array([[1, 2], [2, 3]])
        np.testing.assert_array_equal(matrix, [[1, 2], [2, 3]])


if __name__ == '__main__':
    unittest.main()
