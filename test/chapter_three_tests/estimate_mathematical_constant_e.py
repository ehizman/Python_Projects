import unittest

from chapterThree.estimate_e import find_estimate_of_e_for_nth_term


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_can_find_estimate_of_mathematical_constant_when_term_is_1(self):
        estimate: float = find_estimate_of_e_for_nth_term(1)
        self.assertEqual(1, round(estimate, 2))

    def test_can_find_estimate_of_mathematical_constant_when_term_is_2(self):
        estimate: float = find_estimate_of_e_for_nth_term(2)
        self.assertEqual(round(1 + (1/1), 2), round(estimate, 2))

    def test_can_find_estimate_of_mathematical_constant_when_term_is_3(self):
        estimate: float = find_estimate_of_e_for_nth_term(3)
        self.assertEqual(round(1 + (1/1) + (1/2), 2), round(estimate, 2))

    def test_can_find_estimate_of_mathematical_constant_when_term_is_4(self):
        estimate: float = find_estimate_of_e_for_nth_term(4)
        self.assertEqual(round(1 + (1/1) + (1/2) + (1/6), 2), round(estimate, 2))

    def test_can_find_estimate_of_mathematical_constant_when_term_is_5(self):
        estimate: float = find_estimate_of_e_for_nth_term(5)
        self.assertEqual(round(1 + (1/1) + (1/2) + (1/6) + (1/24), 2), round(estimate, 2))

    def test_can_find_estimate_of_mathematical_constant_when_term_is_6(self):
        estimate: float = find_estimate_of_e_for_nth_term(6)
        self.assertEqual(round(1 + (1/1) + (1/2) + (1/6) + (1/24) + (1/120), 2), round(estimate, 2))


if __name__ == '__main__':
    unittest.main()
