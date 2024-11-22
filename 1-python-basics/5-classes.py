# A simple class
from tkinter.font import names


class Person:
    def show_human(self):
        print("This is human")

person = Person()
person.show_human()

# Class with constructor __init__

class Person:
    def __init__(self, name):
        self.name = name

    def show_human(self):
        print(f'This is {self.name}')

person = Person('Faiza')
person.show_human()

# Class inheritance
class Mammal:
    def __init__(self, name):
        self.name = name

    def intro_message(self):
        print(f'Hey, My name is {self.name}')

class Human(Mammal):
     def secondary_message(self):
        print('I am a human')


class Dog(Mammal):
    def secondary_message(self):
        print('I am a dog')

class Cat(Mammal):
    def secondary_message(self):
        print('I am a cat')

person = Human('Faiza')
dog = Dog('Donny')
cat = Cat('Tom')

person.intro_message()
person.secondary_message()

dog.intro_message()
dog.secondary_message()

cat.intro_message()
cat.secondary_message()

'''
NOTE: Modules in python (similar to JS)
Let's say we have a file printer.py and has two functions, print_my_name, print_my_age.

We can import  and use like,
import printer

printer.print_my_name('Faiza')

We can also do a direct import of the method like
from printer import print_my_name

print_my_name('Faiza')
'''
