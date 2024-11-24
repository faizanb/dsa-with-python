# DNF algorithm (Dutch National Flag) is used for optimal solution
# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    @staticmethod
    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            
            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        print(nums)
        