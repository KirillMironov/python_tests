import unittest
import tensorflow as tf


class TensorFlow1Test(unittest.TestCase):
    def test(self):
        sess = tf.InteractiveSession()
        a = tf.fill([2, 2], 0.5)
        #a = tf.zeros([3, 3])
        print(sess.run(a))


if __name__ == '__main__':
    unittest.main()
