# https://leetcode.com/problems/set-matrix-zeroes/

"""
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""
from typing import List

class Solution:
    def __init__(self):
        pass

    """
    This is a better solution but has some space complexity. 
    Time complexity is O(m*n)
    """
    @staticmethod
    def set_zeroes(matrix: List[List[int]]) -> None:
        zero_index = []
        row_length = len(matrix)
        column_length = len(matrix[0])

        for x in range(row_length):
            for y in range(column_length):
                if matrix[x][y] == 0:
                    zero_index.append([x, y])

        for s in range(len(zero_index)):
            i, j = (0, 0)

            while j < column_length:
                i_index = zero_index[s][0]
                matrix[i_index][j] = 0
                j += 1

            while i < row_length:
                j_index = zero_index[s][1]
                matrix[i][j_index] = 0
                i += 1

    """
    This is the optimal solution with space complexity of O(1).
    Time complexity is O(m*n)
    """

    @staticmethod
    def set_zeroes_optimal(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        column_length = len(matrix[0])

        col0 = 1
        # row tracking = 0th column ----> matrix[...][0]
        # column tracking = col0 (since row0 and col) overlaps + 0th row
        # ----> matrix[0][...]

        for x in range(row_length):
            for y in range(column_length):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    if y == 0:
                        col0 = 0
                    else:
                        matrix[0][y] = 0

        for x in range(1, row_length):
            for y in range(1, column_length):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0

        # Do for column tracking first because it is dependent on matrix[0][0]
        if matrix[0][0] == 0:
            for y in range(0, column_length):
                matrix[0][y] = 0

        if col0 == 0:
            for x in range(0, row_length):
                matrix[x][0] = 0
