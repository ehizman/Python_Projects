import unittest

from chapterThree.factorial_appp import factorial


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_factorial(self):
        factorial_of_number = factorial(5)
        self.assertEqual(120, factorial_of_number)

    def test_factorial_second_time(self):
        factorial_of_number = factorial(3)
        self.assertEqual(6, factorial_of_number)

    def test_factorial_for_0(self):
        factorial_of_number = factorial(10)
        self.assertEqual(3628800, factorial_of_number)

    def test_that_throws_exception_when_negative_number_is_passed(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == '__main__':
    unittest.main()
