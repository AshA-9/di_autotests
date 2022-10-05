import unittest

class TestAbs(unittest.TestCase):
    def test_absolute1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of number")

    def test_absolute2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of number")


if __name__ == "__main__":
    unittest.main()