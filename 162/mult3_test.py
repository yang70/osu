import unittest
from mult3 import mult3
from exception_test import OutOfRangeError

class TestMult3(unittest.TestCase):
    def test_1(self):
        result = mult3(1, 1, 1)
        self.assertEqual(result, 1)

    def test_2(self):
        result = mult3(1, 2, 3)
        self.assertEqual(result, 6)

    def test_3(self):
        result = mult3(1.2, 3.423, 45.2345)
        print(result)
        self.assertAlmostEqual(result, 185.8, 1)

    def test_4(self):
        with self.assertRaises(OutOfRangeError):
            mult3(4, 0, 0)

if __name__ == '__main__':
    unittest.main()