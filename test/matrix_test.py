import unittest
import numpy as np
import random


class MatrixTest(unittest.TestCase):

    def test_matrix(self):
        a1 = [[-1, 1], [2, 0], [0, 3]]
        matrix1 = np.array(a1)
        matrix2 = np.array([[3, 1, 2], [0, -1, 4]])
        result = matrix1 @ matrix2
        np.testing.assert_array_equal(result, [[-3, -2, 2], [6, 2, 4], [0, -3, 12]])

    def createDynamicMatrix(self, rows: int, cols: int):
        matrix = []
        for c in range(0, rows):
            row = []
            for i in range(0, cols):
                row.append(random.randint(-10, 10))
            matrix.append(row)
        return matrix

    def testDynamicMatrix(self):
        matrix1 = np.array(self.createDynamicMatrix(3, 8))
        matrix2 = np.array(self.createDynamicMatrix(8, 7))
        result = matrix1 @ matrix2
        print(result)


if __name__ == '__main__':
    unittest.main()
