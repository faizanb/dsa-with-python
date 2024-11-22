#print function
print("Hello World")

#print * 10 times
print('*' * 10)

#primitives in python
price = 10
rating = 4.8
name = 'Faiza'
is_published = True

# To read input from user on command line
user_name = input('What is your name? ')
fav_color = input('What is your favourite color ')
print(user_name + ' likes ' + fav_color)

#input method always string. To convert to corresponding types use methods like int() float() bool() str()
birth_year = input('Birth year: ')
age = 2024 - int(birth_year)
print('Your age is ' + str(age))

#To get typeof a variable, use type() method returns eg: <class 'int'>
print(type(age))

#To print text that spans multiple lines use 3 quotes(single or double)
text_msg = '''
    Hey Faiza,
        You have a message in your inbox.
        Please do check.
    Thanks.
'''
print(text_msg)

#To access character in a string, use square bracket notation ([]). For reading from the end of the string, use negative indices
course = 'Python program for Beginners'
#Outputs - P
print(course[0])

#Outputs - s
print(course[-1])

#To get substring use [start_index:end_index] syntax, will return substring from start_index to end_index - 1. start_index and end_index are OPTIONAL

#To Output - Python (2 ways)
print(course[0:6])
print(course[:6])

#To Output - Beginners (2 ways)
print(course[19:28])
print(course[19:])

#Below prints the full string as it is
print(course[:])

#Formatted strings f''
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'

'''
Some methods for string operations
course = 'Python for beginners'
len(course)         ------- returns length of the string // 20
course.upper()      ------- returns new string in uppercase // PYTHON FOR BEGINNERS
course.lower()      ------- returns new string in lowercase // python for beginners
course.title()      ------- returns new string in capitalize // Python For Beginners
course.find('P')    ------- returns the index of first occurrence // 0
course.replace('beginners', 'absolute beginners') ------- returns new string with replaced string
'Python' in course  ------- returns Boolean, here True
'''
course = 'Python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('th'))
print(course.replace('beginners', 'absolute beginners'))
print('Python' in course)
print(course)

'''
    Arithmetic operation
    + - * / %
    special division //
    10 / 3  -------- 3.333333335
    10 // 3 -------- 3
    
    10 ** 3 - 1000 ----- exponentiation **
    
    math modules has all methods for mathematical operations
    To do that first import math
'''

import math
#Output - 3
print(math.ceil(2.5))
#Output - 2
print(math.floor(2.5))
#Output - 2.5
print(math.fabs(-2.5))
