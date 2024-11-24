from typing import List

class Solution:

    """ This method generates the one row of pascal triangle"""
    @staticmethod
    def get_row(row_index: int) -> List[int]:
        if row_index == 0:
            return [1]
        elif row_index == 1:
            return [1, 1]

        column_value = 1
        row = [column_value]
        for i in range(1, row_index + 1):
            column_value = int((column_value * ((row_index + 1) - i)) / i)
            row.append(column_value)
        return row

    """ This method generates the entire pascal triangle till num_rows"""
    @staticmethod
    def generate(num_rows: int) -> List[List[int]]:
        row = []
        if num_rows == 1:
            row.append([1])
            return row
        elif num_rows == 2:
            row.append([1])
            row.append([1, 1])
            return row

        row.append([1])
        for i in range(1, num_rows):
            previous_value = 1
            column = [previous_value]
            for j in range(1, i + 1):
                previous_value = int((previous_value * ((i + 1) - j)) / j)
                column.append(previous_value)
            row.append(column)

        return row