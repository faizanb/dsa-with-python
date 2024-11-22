
from typing import  List


def partition(array: List[int], low, high) -> int:
    pivot = array[low]
    i = low
    j = high

    while i < j:
        while array[i] <= pivot and i < high:
            i += 1
        while array[j] > pivot and j > low:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    array[j], array[low] = array[low], array[j]
    return j

def quick_sort(array: List[int], first: int, last: int) -> List[int]:
    if first < last:
        partition_index = partition(array, first, last)
        print(f'partition_index: {partition_index}')
        quick_sort(array, first, partition_index - 1)
        quick_sort(array, partition_index + 1, last)

    return array


if __name__ == '__main__':
    array_len = int(input('Enter array length > '))
    array_input = input('Enter array > ')
    unsorted_array = [int(value) for value in array_input.split()]
    print(f'Sorted array is {quick_sort(unsorted_array, 0, array_len - 1)}')
