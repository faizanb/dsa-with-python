from typing import List

class Solution:
    @staticmethod
    def print_max_sub_array(self, nums: List[int]) -> int:
        # print max subarray with Kadane's algorithm
        sum = 0
        max = sum
        start_index = 0
        end_index = 0
        for i in range(len(nums)):
            if sum == 0:
                start_index = i
            sum += nums[i]
            if sum < 0:
                sum = 0
            elif sum > max:
                max = sum
                end_index = i

        print(f'Max sub array with sum {max} is {nums[start_index:end_index + 1]}')
        return max


if __name__ == '__main__':
    solution = Solution()
    print(f'Max sum is {solution.print_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])}')
