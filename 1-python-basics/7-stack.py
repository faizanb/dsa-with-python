from inspect import stack
from typing import List

class Stack:
    def __init__(self):
        self.stack: List[int] = []

    def add_to_stack(self, data):
        self.stack.append(data)
        print(f'{data} pushed to stack', end='\n')

    def peek_stack(self):
        print(f'Top element in stack is {self.stack[-1]}', end='\n')

    def remove_from_stack(self):
        removed = self.stack.pop()
        print(f'Removed {removed} from stack', end='\n')

if __name__ == '__main__':
    program_input = [input() for _ in range(int(input()))]
    stack_obj = Stack()
    for value in program_input:
        stack_obj.add_to_stack(value)
    print(f'Stack is {stack_obj.stack}', end='\n')

    stack_obj.peek_stack()
    stack_obj.remove_from_stack()
    stack_obj.peek_stack()
    stack_obj.add_to_stack(5)




