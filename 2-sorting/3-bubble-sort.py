"""
    BUBBLE SORT
    Select the largest element and bubble it up to the top of the array

    Worst and average complexity of this algorithm is O(n2)
    Best case time complexity, ie if the array is sorted in O(n)
"""

from typing import List

def bubble_sort(array: List[int]) -> List[int]:
    array_len = len(array)
    for i in reversed(range(array_len)):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == '__main__':
    arr_length = int(input('Enter Array length > '))
    program_input = input("Enter input array > ")
    input_array = [int(value) for value in program_input.split()]
    sorted_array = bubble_sort(input_array)
    print(f'Sorted array is {sorted_array}', end="\n")