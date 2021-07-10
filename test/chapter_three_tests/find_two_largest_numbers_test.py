import unittest

from chapterThree.find_two_largest_numbers import find_two_largest_numbers_in


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_find_two_largest_numbers_in_a_list(self):
        a_list = [0, 1, 3, 5, 7, 7, 6, 13, 8, 9]
        result_as_tuple = find_two_largest_numbers_in(a_list)
        self.assertEqual((13, 9), result_as_tuple)


if __name__ == '__main__':
    unittest.main()
