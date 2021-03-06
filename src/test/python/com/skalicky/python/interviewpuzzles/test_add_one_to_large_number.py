from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.add_one_to_large_number import Solution


class TestSolution(TestCase):
    def test_add_one_to_large_number__when_lower_digits_overflow__then_higher_digit_is_incremented(self):
        self.assertListEqual([3, 0, 0], Solution.add_one_to_large_number([2, 9, 9]))

    def test_add_one_to_large_number__when_0_as_one_digit_number__then_1(self):
        self.assertListEqual([1], Solution.add_one_to_large_number([0]))

    def test_add_one_to_large_number__when_no_digit_overflows__then_only_lowest_digit_is_incremented(self):
        self.assertListEqual([2, 3, 5], Solution.add_one_to_large_number([2, 3, 4]))

    def test_add_one_to_large_number__when_all_digits_overflow__then_all_digits_are_set_0_and_new_highest_digit_1_is_added(
            self):
        self.assertListEqual([1, 0, 0, 0], Solution.add_one_to_large_number([9, 9, 9]))
