"""
    SELECTION SORT
    Select the smallest element in the array and swap so that it is pushed to the front
    Further iteration will be on sub-array from next index (i+1)

    Worst and average complexity of this algorithm is O(n2)
    Best case time complexity, ie if the array is sorted in O(n)
"""

from typing import List

def selection_sort(array: List[int]) -> List[int]:
    array_len = len(array)

    for i in range(array_len):
        minimum = array[i]
        min_index = i
        # Inner loop runs from i+1 to n and swaps with i,
        # if any of the value from i+1 to n is less than value at i
        for j in range(i + 1, array_len):
            if array[j] < minimum:
                minimum = array[j]
                min_index = j
        if min_index == i and i == 0:
            break
        else:
            array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == '__main__':
    arr_length = int(input('Enter Array length > '))
    program_input = input("Enter input array > ")
    input_array = [int(value) for value in program_input.split()]
    sorted_array = selection_sort(input_array)
    print(f'Sorted array is {sorted_array}', end="\n")