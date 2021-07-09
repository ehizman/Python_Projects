import unittest
from classwork.get_length import get_length_from_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_length(self):
        new_list = [1, 4, 5, 6, 7]
        result = get_length_from_list(new_list)
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()
