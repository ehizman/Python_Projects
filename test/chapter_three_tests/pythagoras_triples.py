import unittest

from chapterThree.pythagora_triple import is_pythagoras_triple


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_pythagoras_triple(self):
        self.assertFalse(is_pythagoras_triple(10, 4, 6))


if __name__ == '__main__':
    unittest.main()
