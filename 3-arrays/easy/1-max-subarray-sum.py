from typing import List

class Solution:
    @staticmethod
    def max_sub_array(self, nums: List[int]) -> int:
        # Optimal solution is using Kadane's algorithms
        # algorithm states that at any moment sum goes less than 0, reset sum to 0
        # if all array elements are negative, return the greatest of them which will be the maximum sum,
        # this is handled with max_so_far variable
        sum = 0
        max_sum = sum
        max_so_far = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 0:
                sum = 0
            elif sum > max_sum:
                max_sum = sum
            if nums[i] > max_so_far:
                max_so_far = nums[i]

        return max_sum if max_so_far > 0 else max_so_far