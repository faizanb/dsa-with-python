from typing import List

class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end_of_ll(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def print_linked_list(self):
        node = self.head
        while node is not None:
            if node.next is None:
                print(node.data)
            else:
                #To keep printing on the same line
                print(node.data, end=" > ")
            node = node.next
        if node is self.head:
            print('Linked list is empty')

def execute(program: List[str]):
    linked_list = LinkedList()
    for data in program:
        linked_list.insert_at_end_of_ll(data)
    linked_list.print_linked_list()

if __name__ == "__main__":
    program_input = [input() for _ in range(int(input('Enter size of linked list')))]
    execute(program_input)
