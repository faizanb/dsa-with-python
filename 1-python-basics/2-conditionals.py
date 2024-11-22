# Program 1 - with conditional operators
name = 'Jane Smith'

if len(name) < 3:
    print('Name should at least be 3 characters')
elif len(name) >= 50:
    print('Name should not exceed 50 characters')
else:
    print('Name looks good!')

# Program 2 - boolean check
has_good_credit = True
price = 50000

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print('Your down payment is ' + str(down_payment))

# Program 3 - with logical operators - and, or, not
has_high_income = True
has_good_credit = False
has_criminal_record = False
if (has_high_income or has_good_credit) and not has_criminal_record:
    print('Eligible for purchase')
else:
    print('Not eligible for purchase')

