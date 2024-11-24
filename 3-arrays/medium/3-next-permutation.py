from typing import List

class Solution:
    @staticmethod
    def next_permutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_length = len(nums)

        break_point = -1
        # Find the breakpoint at which swap has to be done
        for i in range(nums_length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break

        # The array is in its last permutation, ie [ 3 2 1 ]
        # print the first array [1 2 3 ] in this case which is going to be the next permutation
        if break_point == -1:
            print(nums.reverse())
            return

        # Find the next largest number to swap with number at breakpoint
        for i in range(nums_length - 1, break_point, -1):
            if nums[i] > nums[break_point]:
                nums[break_point], nums[i] = nums[i], nums[break_point]
                break

        # Reverse nums from break_point + 1 to last index to get the next permutation
        nums[break_point + 1:] = reversed(nums[break_point + 1:])

        print(nums)

