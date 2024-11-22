# Dictionaries - new keys can be added like customer[key] = value
from multiprocessing.managers import Value

customer = {
    "name": "Faiza",
    "age": 29,
    "is_verified": True
}

# This will throw an error if key doesn't exist
print("Customer Name: " + customer["name"])

# To handle it gracefully, use get method. optional default value can also be given
# Will give None
print("Birth Date: " + str(customer.get("birth_date")))
# Will return the default value
print("Birth Date: " + customer.get("birth_date", "Jan 01 1970"))

# FUNCTIONS - use def keyword
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome on board :)')

print('Start')
greet_user('Faiza')
greet_user('Robin')
print('Finish')

'''
keyword arguments vs positional arguments. Keyword arguments gives meaning to the arguments
that you pass into a function. You don't need to follow the order of the arguments in this case.
For positional arguments, you simply pass the argument values in the right order.
Only use keyword arguments when you want to improve the readability for your code.
'''
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard!')

# Positional Arguments
greet_user('John', 'Smith')

# Keyword Arguments
greet_user(last_name='Smith', first_name='John')

# Functions returning value.
# If a function does not have a return statement by default python returns None
def square(number):
    return number * number

result = square(4)
print(f'result: {result}')

# try except in python.
# NOTE: can be used outside functions as well
# error type to be excepted has to be defined after except key
# NOTE: you can get the exception error type from the console
def get_risk_factor():
    try:
        age = int(input('Enter Age > '))
        income = 200
        risk = income/age
        print(age)
    except ValueError:
        print('Invalid age. Age should be number')
    except ZeroDivisionError:
        print('Age cannot be zero')

get_risk_factor()