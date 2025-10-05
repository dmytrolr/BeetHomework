import unittest
from main import choose_func, square_nums, remove_negatives


class TestChooseFunc(unittest.TestCase):

    def test_all_positive(self):
        self.assertEqual(choose_func([1, 2, 3], square_nums, remove_negatives), [1, 4, 9])

    def test_with_negatives(self):
        self.assertEqual(choose_func([-1, 2, -3, 4], square_nums, remove_negatives), [2, 4])

    def test_all_negative(self):
        self.assertEqual(choose_func([-5, -2, -1], square_nums, remove_negatives), [])

    def test_empty_list(self):
        self.assertEqual(choose_func([], square_nums, remove_negatives), [])


if __name__ == '__main__':
    unittest.main()
