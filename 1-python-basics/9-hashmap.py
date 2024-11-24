# We use dictionary (refer basics) to implement hashmap

from typing import Dict, List

class HashMap:
    def __init__(self):
        self.counter: Dict[int, int] = {}

    def insert_to_map(self, value):
        if value in self.counter:
            self.counter[value] += 1
        else:
            self.counter[value] = 1

    def return_from_map(self, value):
        if value in self.counter:
            return print(f'Counter map of {value} is {self.counter[value]}', end='\n')
        print(f'Element not found in map', end='\n')

if __name__ == '__main__':
    input_num = int(input('Enter number of inputs > '))
    hashmap = HashMap()
    for _ in range(input_num):
        program_input = int(input('Enter value > '))
        hashmap.insert_to_map(program_input)

    hashmap.return_from_map(1)