import unittest
import math
import random
import miniball


class TestMiniball(unittest.TestCase):
    def test_2d_miniball(self):
        P = [(1, 1), (-1, -1)]
        mb = miniball.Miniball(P)
        self.assertEqual(mb.center(), [0, 0])
        self.assertEqual(mb.squared_radius(), 2)

    def test_3d_miniball(self):
        P = [(1, 1, 1), (-1, -1, -1)]
        mb = miniball.Miniball(P)
        self.assertEqual(mb.center(), [0, 0, 0])
        self.assertEqual(mb.squared_radius(), 3)


if __name__ == "__main__":
    unittest.main()
