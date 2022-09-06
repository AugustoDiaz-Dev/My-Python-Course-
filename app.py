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


