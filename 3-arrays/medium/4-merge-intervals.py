# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        return_arr = []
        return_arr.append(intervals[0])

        for i in range(1, len(intervals)):
            r_len = len(return_arr)
            if intervals[i][0] > return_arr[r_len - 1][1]:
                return_arr.append(intervals[i])
            elif intervals[i][0] <= return_arr[r_len - 1][1] and intervals[i][1] > return_arr[r_len - 1][1]:
                return_arr[r_len - 1] = [return_arr[r_len - 1][0], intervals[i][1]]

        return return_arr




