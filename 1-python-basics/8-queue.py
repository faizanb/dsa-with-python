# Deque is used for this.
# It allows operations like pop, popleft, append, appendleft

from collections import deque
from typing import Deque, List

class Queue:
    def __init__(self):
        self.queue: Deque[int] = deque()

    def insert_to_queue(self, data):
        self.queue.append(data)

    def delete_from_queue(self):
        print(f'{self.queue.popleft()} popped from queue', end='\n')

    def peep_queue(self):
        print(f'Peek into queue {self.queue[0]}', end='\n')

if __name__ == '__main__':
    program_input = [input() for _ in range(int(input('Enter length of queue > ')))]
    queue_obj = Queue()
    for value in program_input:
        int_value = int(value)
        queue_obj.insert_to_queue(int_value)
    print(f'Queue is {queue_obj.queue}', end='\n')

    queue_obj.peep_queue()
    queue_obj.delete_from_queue()
    queue_obj.peep_queue()
