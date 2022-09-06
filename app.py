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
# Then print a message using that data. E.G.
# "Hi I am Augusto and my favorite food is fish".
favorite_food = input('What is your favorite food? ')
print('Hi, my name is ' +name + ' and my favorite food is ' +favorite_food + '.')
