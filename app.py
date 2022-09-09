# print method
print('Hi Augusto!')
# Python code gets executed line by line from top to bottom
print('O----')
print('||||')
# Types of data
# This is called "an expression". An expression is a piece of code that produces a value.
print('*' * 10)
# TASK 1 Try to draw another shape or letter, or animal.
print('-----')
print('  |  ')
print('  |  ')
print('  |  ')

# Variables (identifier, assignation, value)
price = 10
price = 20
print(price)
# Integers and floats
apples = 5
rating = 4.5
name = 'Augusto'
is_published = True
print(rating)
# Python is a case-sensitive language. When defining variables we always have to use lower case (snake case).
# Task 2 - At School. We have a student called George Harrison. He's 8 years old and is a new student.
# Define three variables: age, full_name and is_new_student.
full_name = 'George Harrison'
age = 20
is_new_student = True

# input method
name = input('What is your name? ')
print('Hi ' + name + '!')
# Task 3. Extend this program and ask the person's name and favorite food.
# Then print a message using that data. E.G.
# "Hi I am Augusto and my favorite food is fish".
favorite_food = input('What is your favorite food? ')
print('Hi, my name is ' +name + ' and my favorite food is ' +favorite_food + '.')

# Calculate age from the birth year. int() float() str() bool()
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)
# Task 4. Write a program to ask to the user their weight (in pounds),
# convert it to kilograms and print on the terminal.
weight_in_kilograms = input('Weight: ')
print(type(weight_in_kilograms))
weight_in_pounds = int(weight_in_kilograms) * 2.2046
print(weight_in_pounds)

# simple, double and triple quotes.
course = "Python's for beginners"
print(course)
# triple quotes
message = '''
Hi John
Welcome to our Python Course. 
Thanks for your support. 
'''
print(message)
# Index
my_course = "Scratch for beginners"
print(my_course[0])
print(my_course[-2])
print(my_course[0:3])
print(my_course[0:])
print(my_course[1:])
print(my_course[:5])
print(my_course[:]) # You can copy or clone your string
another_course = my_course[:]

# Task 5. What happens in this scenario?
name = 'Anna'
print(name[1:-1]) # Returns nn

# Formatted strings  f'{}'
# this code works but is not optimal
first =  'Augusto'
last = 'Diaz'
message = first + ' [' + last + '] is a coder'
print(message)
# The same code using formatted strings
msg = f'{first} [{last}] is a coder'
print(msg)

# String methods
course = 'Python for Beginners.'
print(len(course)) # len() & print() are general purpose functions
print(course.upper()) # upper() method
print(course) # the original string doesn't change
print(course.lower())
print(course.find('P')) # gives you the index
print(course.find('O')) # find() is case sensitive. Here it will return -1
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course) # boolean expression

# Arithmetic Operations
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
# using augmented assignment operator
x = 10
x = x + 3
print(x)
x += 3
x -= 3
print(x)

#Operator precedence
w = 10 + 3 * 2
print(w)
x = 10 + 3 * 2 * 2 ** 2
print(x)
y = (10  + 3) * 2 ** 2
print(y)
z = (2 + 3) * 10 - 3
print(z)
# Order of precedence:
# parenthesis
# exponentiation 2 ** 3
# multiplication or division
# addition or subtraction

# Math functions
import math # math module
# built in functions
x = 2.9
print(round(x))
print(abs(-2.9)) # always returns the positive representation of that value

print(math.ceil(x))
print(math.floor(x))

# check out the docs for more methods: https://docs.python.org/3/library/math.html

# Conditions
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's a lovely day!")
# Task 6.
# Price of a house is $ 1 million.
# If buyer has good credit,
#   they need to put down 10%
# otherwise
#   they need to put down 20%
# print the down payment
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: $ {down_payment}")

# Logical operators
# if applicant has high income AND good credit
#   Eligible for loan
# logical AND: both conditions should be true
has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for loan.")
else:
    print('Not eligible.')

# logical OR: at least one of the conditions should be true
# if applicant has high income OR good credit
#   Eligible for loan
if has_high_income or has_good_credit:
    print("Eligible for loan.")
# logical NOT
# if applicant has good credit AND doesn't have a criminal record
if has_good_credit and not has_criminal_record:
    print('Eligible for loan.')
else:
    print('Not eligible')
    
# Comparison operators - < > <= >= == !=
# if temperature is greater than 30
#   it's a hot day
# otherwise if it's less than 10
#   it's a cold day
# otherwise
#   it's neither hot nor cold
temperature = 9
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("It's neither hot nor cold")

# Task 7
# if name is less than 3 characters long
#   name must be at least 3 characters
# otherwise if it's more than 50 characters long
#   name must be a maximum of 50 characters
# otherwise
#   name looks good!
name = 51
if name < 3:
    print("Name must be at least 3 characters")
elif name >= 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")
    
# Project Weight Converter
# Show to the student the final program and then they should write by themselves
weight = int(input("Weight: "))
lbs_or_kg = input("(L)bs or (K)g: ")
result = 0;
if lbs_or_kg.upper() == 'L':
    converted = weight * 0.45
    print(f'Your weight is {converted} kilos.')
else:
    converted = weight / 0.45
    print(f'Your weight is {converted} pounds.')
    
# While loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done!")

i = 0
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done!")


# useful python modules: Math
