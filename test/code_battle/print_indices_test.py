import unittest

from code_battle.print_indices import return_indices_of_elements_that_sum_to_number_to_find


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_can_return_sum_of_indices(self):
        list_ = [1, 4, 6, 7, 9]
        number_to_find = 5
        returned_indices = return_indices_of_elements_that_sum_to_number_to_find(list_, number_to_find)
        self.assertListEqual([0, 1], returned_indices)

    def test_can_return_sum_of_indices_for_many(self):
        list_ = [1, 4, -11, 7, 9]
        number_to_find = -10
        returned_indices = return_indices_of_elements_that_sum_to_number_to_find(list_, number_to_find)
        self.assertListEqual([0, 2], returned_indices)


if __name__ == '__main__':
    unittest.main()
