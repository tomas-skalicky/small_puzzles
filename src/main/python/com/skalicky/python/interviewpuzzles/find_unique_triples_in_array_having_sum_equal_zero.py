# Task:
#
# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that
# a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be
# duplicates.
#
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]
# Here's a starting point:
#
# class Solution(object):
#   def threeSum(self, nums):
#     # Fill this in.
#
# # Test Program
# nums = [1, -2, 1, 0, 5]
# print(Solution().threeSum(nums))
# # [[-2, 1, 1]]
from typing import Dict, List, Set, Tuple


class Solution:
    @staticmethod
    def three_sum(nums: List[int]) -> Set[Tuple[int, int, int]]:
        """Time complexity is O(n^2)
        """

        number_count: int = len(nums)
        if number_count < 3:
            return set()
        else:
            # Time complexity of sorting is O(n log n)
            sorted_numbers: List[int] = sorted(nums)

            number_dictionary: Dict[int, int] = {}
            for i in range(0, number_count):
                current_number: int = sorted_numbers[i]
                if current_number in number_dictionary:
                    number_dictionary[current_number] += 1
                else:
                    number_dictionary[current_number] = 1

            # The data structure Set ensures uniqueness of Tuples.
            result_set: Set[Tuple[int, int, int]] = set()

            # Time complexity of the following two nested loops is O(n^2).
            for i in range(0, number_count - 2):
                # +2 to allow one index in between
                for j in range(i + 2, number_count):
                    i_number: int = sorted_numbers[i]
                    j_number: int = sorted_numbers[j]
                    lookup_number: int = - (i_number + j_number)
                    if i_number < lookup_number < j_number \
                            or lookup_number == i_number == sorted_numbers[i + 1] \
                            or lookup_number == j_number == sorted_numbers[j - 1]:
                        result_set.add((i_number, lookup_number, j_number))
            return result_set


print(Solution.three_sum([0, 0, 0]))
# [[0, 0, 0]]
print(Solution.three_sum([1, -2, 1, 1]))
# [[-2, 1, 1]]
print(Solution.three_sum([1, -2, 1, 0, 5]))
# [[-2, 1, 1]]
print(Solution.three_sum([0, -1, 2, -3, 1]))
# [[0, -1, 1], [2, -3, 1]]
