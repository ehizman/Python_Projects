import unittest

from object_oriented_programming_in_python.Time_Class import Time_Class


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_Constructor(self):
        Time_Class(self, 12, 55, 4)


if __name__ == '__main__':
    unittest.main()
