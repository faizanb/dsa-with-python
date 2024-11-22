# While loop - Guess Game
secret_number = 56
guess_count = 1
guest_try = 5

print(f'You need to guess a number between 1 - 100. You have {guest_try} tries!')

while guess_count <= guest_try:
    user_guessed = int(input('Guess> '))
    if user_guessed == secret_number:
        print('You Won!')
        break
    print('Incorrect. Try again')
    guess_count = guess_count + 1
# This is else block for while loop, if break happens from loop at the full iteration counts
else:
    print('You failed.')


#For loops
'''
for item in 'Python':
    print(item)

for item in ['My', 'Name', 'is', 'Faiza']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

#If the range of numbers is too large, you can use range function
# Below outputs 0 to 4
for item in range(5):
    print(item)
'''
# Below iterates from i = 5 to i = 10, after each iteration increments by 2
for i in range(5, 10, 2):
    print(i)

# NESTED Loops
number = [5, 2, 5, 2, 2]
print('Generate an F figure')

for x in number:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)

#List methods
'''
    append(value) - to append to the end of the list
    insert(index, value) - to add to anywhere in the list by passing index
    pop() - to remove last item in the list
    index(value) - to check if value exists. similar to 'value in list' check
    sort() - to sort the list
    sort() then reverse() - to sort the list in descending order
    copy() - returns a copy of the original list
'''

# Program to remove duplicates in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for value in numbers:
    if value not in uniques:
        uniques.append(value)
print("Unique array is: " + str(uniques))

# Tuples vs Lists - Tuples are immutable items, so cannot do any changes on tuple
# TUPLES
numbers = (1, 2, 3)
print(numbers[0])

# LIST
new_numbers = [1, 2, 3]

# Unpacking in tuples and lists
cord = (1, 2, 3)
x, y, z = cord
