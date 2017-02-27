import unittest
from EulerProject15 import recursive


class MyTestCase(unittest.TestCase):
    def test_h_one_w_zero_returns_one(self):
        self.assertEqual(1, recursive(1,0))

    def test_h_zero_w_one_returns_one(self):
        self.assertEqual(1, recursive(0,1))

    def test_h_one_w_one_returns_two(self):
        self.assertEqual(2, recursive(1,1))

    def test_h_two_w_zero_returns_one(self):
        self.assertEqual(1, recursive(2,0))

    def test_h_zero_w_two_returns_one(self):
        self.assertEqual(1, recursive(0,2))

if __name__ == '__main__':
    unittest.main()
