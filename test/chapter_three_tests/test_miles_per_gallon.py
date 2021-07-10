import unittest


from chapterThree.miles_per_gallon import average_miles_per_gallon


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_returns_average_miles_per_gallon(self):
        average: float = average_miles_per_gallon(12.8, 287)
        self.assertEquals(22.42, average)

    def test_throws_exception_when_invalid_input_is_tried_to_be_entered(self):
        with self.assertRaises(ZeroDivisionError):
            average_miles_per_gallon(-123, 12.8)


if __name__ == '__main__':
    unittest.main()
