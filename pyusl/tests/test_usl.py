from unittest import TestCase

from pyusl import *

class TestUSL(TestCase):
    def test_constructor(self):
        u = usl()
        self.assertTrue(isinstance(u, usl))
        self.assertEqual(u.gamma, 1)
        self.assertEqual(u.alpha, 0)
        self.assertEqual(u.beta, 0)

    def test_constructor_inputs(self):
        u = usl(3,4,5)
        self.assertEqual(u.gamma, 3)
        self.assertEqual(u.alpha, 4)
        self.assertEqual(u.beta, 5)
        self.assertIsNone(u.rawx)
        self.assertIsNone(u.rawy)
