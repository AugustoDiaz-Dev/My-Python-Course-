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


# Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else:
    print('Sorry, you failed.')
    
    
# Car game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == 'help':
        print("""
start - to stat the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")

        
# For loops
for item in 'Python':
    print(item)

for item in ['John', 'Paul', 'Ringo', 'George']:
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in range(1, 10, 2): # This is an object
    print(item)

# Task 8. Calculate the total cost of our shopping cart.
prices = [10, 20, 30];
total = 0
for price in prices:
    total += price
print(f'Total: $ {total}')


# Nested loops
for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')
# Task 9. Draw a F shape with nested loops.
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
# Task 10 modify the numbers to print an L.
numbers = [2,2,2,6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

    
# Lists.
# When you use square brackets it returns a new list. The original is not modified.
names = ["Peter", "Bruce", "Sarah", "Mary", "Augusto"]
print(names)
print(names[0])
print(names[-2])
print(names[2:])
print(names[2:4])
print(names[:])
names[0] = 'Pe'
print(names)
# Task 11. Write a program to find the largest number in a list.
numbers_list = [3,6,2,8,4, 10]
max = numbers[0]
for number in numbers_list:
    if number > max:
        max = number
print(max)


# 2D lists
'''
[
    1 2 3
    4 5 6
    7 8 9
]
3x3
'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1] = 20
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

        
 # List methods
numbers = [5,2,1,7,4,6, 5]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(4)
# numbers.clear()
numbers.pop()
print(numbers.index(7))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
# Task 12. Write a program to remove the duplicates in a list.
numbers = [2,4,4,6,6,6,8,8,8,8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Tuples ().
# They are inmutable.
my_numbers = (1,2,3)
print(my_numbers[0])
print(my_numbers)


# Unpacking
coordinates = (1,2,3)
x, y, z = coordinates
print(y)
   
# Dictionaries - key value pairs
customer = {
    "name": "Augusto Diaz",
    "age": 39,
    "is_verified": True
}
customer["name"] = 'Augusto Roberto Diaz'
customer["is_new"] = True
print(customer["name"]) # If there is not match returns an error
print(customer.get("age")) # If there is not match returns None
print(customer.get("birth_date", "June 11 1983"))
print(customer)
# Task 13. Phone number converter
phone_number = input("Phone: ")
digits = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for number in phone_number:
    output += digits.get(number, "!") + " "
print(output)
# Emoji converter :) with dictionaries
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😄",
    ":(": "☹"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


# Functions
def greet_user():
    print("Hi there!")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")

# Parameters
# Parameters are the placeholders and arguments are the information supplied
def greet_user(name, last_name):
    print(f"Hi {name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("Augusto", "Diaz")
print("Finish")


# Keyword arguments
# If you are dealing with numerical values without not a clear explanation of what they represent use keyword arguments.
# Keyword arguments should always go after a positional argument.
def greet_user(name, last_name):
    print(f"Hi {name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(last_name="Diaz", name="Augusto")
print("Finish")


# Return statement
def square(number):
    return number * number
result = square(3)
print(result)
print(square(4))


# Creating a reusable function
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😄",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))


# Exceptions
# They are used to handle exceptions that are raised in our programs
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value.")

    
# Comments
# This line is going to be ignored because is a comment
print("Sky is blue")


# Classes
# The class is the blueprint for creating new objects.
# An object is an instance of a class.
# Each object can have methods and attributes
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point1 = Point()
point1.x =  10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)


# Constructors
# The constructor is a function that gets called at the time of creating an object.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Point(10, 20,)
point.x = 11
print(point.x)
# Task 14. Define a class Person with name and talk()
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}.')


augusto = Person('Augusto Diaz')
augusto.talk()


# Inheritance
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
