import unittest
import tensorflow as tf
import numpy as np


class TensorFlow1Test(unittest.TestCase):
    def test(self):
        sess = tf.InteractiveSession()
        a = tf.fill([2, 2], 0.5)
        print(sess.run(a))

    def test_1(self):
        sess = tf.InteractiveSession()
        x = tf.Variable(tf.random_normal([1]), name='x')
        y = tf.pow(x - 1, 2)
        gd = tf.train.GradientDescentOptimizer(0.001)
        train_step = gd.minimize(y)
        sess.run(tf.global_variables_initializer())

        train_errors = []

        for i in range(1, 100):
            _, train_err = sess.run([train_step, y])
            train_errors.append(train_err)

        print(train_err)


if __name__ == '__main__':
    unittest.main()
