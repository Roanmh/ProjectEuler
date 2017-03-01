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

    def test_h_two_w_one_returns_one(self):
        self.assertEqual(3, recursive(2,1))

    def test_h_one_w_two_returns_one(self):
        self.assertEqual(3, recursive(1,2))

    def test_h_two_w_two_returns_one(self):
        self.assertEqual(6, recursive(2,2))

    def test_h_two_w_three_returns_one(self):
        self.assertEqual(10, recursive(2,3))

    def test_h_three_w_two_returns_one(self):
        self.assertEqual(10, recursive(3,2))

if __name__ == '__main__':
    unittest.main()
