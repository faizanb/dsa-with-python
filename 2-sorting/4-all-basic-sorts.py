
from typing import List

def selection_sort(array: List[int]) -> List[int]:
    array_len = len(array)

    for i in range(array_len):
        min_index = i
        min_value = array[i]
        for j in range(i + 1, array_len):
            if array[j] < min_value:
                min_index = j
                min_value = array[j]
        array[i], array[min_index] = array[min_index], array[i]

    return array


def bubble_sort(array: List[int]) -> List[int]:
    array_len = len(array)
    for i in reversed(range(array_len)):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def insertion_sort(array: List[int]) -> List[int]:
    array_len = len(array)
    for i in range(array_len):
        for j in reversed(range(i, 0)):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array


if __name__ == '__main__':
    unsorted_array_len = int(input('Enter array length > '))
    unsorted_array_inp = input('Enter array input > ')
    unsorted_array = [int(value) for value in unsorted_array_inp.split()]
    print(f'Unsorted array is > {unsorted_array}', end='\n')
    print(f'Sorted array is (selection sort) > {selection_sort(unsorted_array)}', end='\n')
    print(f'Sorted array is (bubble sort) > {bubble_sort(unsorted_array)}', end='\n')
    print(f'Sorted array is (insertion sort) > {insertion_sort(unsorted_array)}', end='\n')