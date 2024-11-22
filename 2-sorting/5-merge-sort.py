
from typing import  List


def merge(array: List[int], first: int, mid: int, last: int) -> List[int]:
    left_index = first
    right_index = mid + 1
    temp: List[int] = []

    while (left_index <= mid) and (right_index <= last):
        if array[left_index] <= array[right_index]:
            temp.append(array[left_index])
            left_index += 1
        else:
            temp.append(array[right_index])
            right_index += 1

    while left_index <= mid:
        temp.append(array[left_index])
        left_index += 1

    while right_index <= last:
        temp.append(array[right_index])
        right_index += 1

    for i in range(first, last + 1):
        array[i] = temp[i-first]

    return array

def merge_sort(array: List[int], first: int, last: int) -> List[int]:
    if first == last:
        return [array[first]]
    mid = int((first + last) / 2)
    merge_sort(array, first, mid)
    merge_sort(array, mid + 1, last)
    return merge(array, first, mid, last)


if __name__ == '__main__':
    array_len = int(input('Enter array length > '))
    array_input = input('Enter array > ')
    unsorted_array = [int(value) for value in array_input.split()]
    print(f'Sorted array is {merge_sort(unsorted_array, 0, array_len - 1)}')
