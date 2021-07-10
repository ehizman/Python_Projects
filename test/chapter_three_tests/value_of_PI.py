import unittest

from chapterThree.estimate_pi import estimate_pi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_can_evaluate_the_value_of_PI_for_first_term(self):
        value_of_pi: float = estimate_pi(1)
        self.assertEqual(4.0, value_of_pi)

    def test_can_evaluate_the_value_of_PI_for_second_term(self):
        value_of_pi: float = estimate_pi(2)
        self.assertEqual(4 - (4/3), value_of_pi)

    def test_can_evaluate_the_value_of_PI_for_third_term(self):
        value_of_pi: float = estimate_pi(3)
        self.assertEqual(4 - (4/3) + (4/5), value_of_pi)

    def test_can_evaluate_the_value_of_PI_for_fourth_term(self):
        value_of_pi: float = estimate_pi(4)
        self.assertEqual(4 - (4/3) + (4/5) - (4/7), value_of_pi)

    def test_raises_Value_Error_exception_when_zero_is_passed_in_as_parameter(self):
        with self.assertRaises(ValueError):
            value_of_pi: float = estimate_pi(0)


if __name__ == '__main__':
    unittest.main()
