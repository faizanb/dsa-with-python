"""
    INSERTION SORT
    Always insert the element to its correct position by shifting all the elements to right and
    inserting at the correct index.
    After every iteration, the subarray size grows by 1 and all the elements in
    the subarray gets placed into its correct position by doing a left swap from the end

    Worst and average complexity of this algorithm is O(n2)
    Best case time complexity, ie if the array is sorted in O(n)
"""

from typing import List

def insertion_sort(array: List[int]) -> List[int]:
    array_len = len(array)

    for i in range(array_len):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1
    return array


if __name__ == '__main__':
    arr_length = int(input('Enter Array length > '))
    program_input = input("Enter input array > ")
    input_array = [int(value) for value in program_input.split()]
    sorted_array = insertion_sort(input_array)
    print(f'Sorted array is {sorted_array}', end="\n")