import unittest
from chapterThree.palindrome import is_palindrome


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_palindrome_app_returns_true_when_a_palindrome_is_passed(self):
        number: int = 56765
        self.assertTrue(is_palindrome(number))

    def test_palindrome_app_returns_false_when_a_non_palindrome_is_passed(self):
        number: int = 56664
        self.assertFalse(is_palindrome(number))

if __name__ == '__main__':
    unittest.main()
