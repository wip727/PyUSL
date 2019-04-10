from unittest import TestCase

import numpy as np
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

    def test_fit(self):
        u = usl(3,4,5)
        x = [1,3,6]
        y = [2,6,12]
        u.fit(x, y, requires_plot = False)
        self.assertAlmostEqual(u.gamma, 2, places=5)
        self.assertAlmostEqual(u.alpha, 0, places=5)
        self.assertAlmostEqual(u.beta, 0, places=5)
        self.assertEqual(u.rawx, x)
        self.assertTrue(u.rawy, y)

    def test_compute(self):
        u = usl([1,2,3])
        x = np.array([1,3,6])
        y_act = u.compute(x)
        y_exp = u.gamma * x / (1 + u.alpha * (x - 1) + u.beta * x * (x - 1))
        # assertEqual does not work with np.array
        np.testing.assert_array_equal(y_act, y_exp)
