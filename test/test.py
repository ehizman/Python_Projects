import unittest

from classwork.return_length_and_sum_of_a_list import get_mean


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_get_mean(self):
        result = get_mean([1, 5, 6])
        self.assertEqual(result, (3, 12))


if __name__ == '__main__':
    unittest.main()
