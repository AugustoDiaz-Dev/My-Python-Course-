#Topic: Functions.

#"def" is short for “define”. It's a keyword that you need to define a function (aka method). All the code that you put between the def function_name(parameters) and end will be executed every time you call the function_name later.
#"A parameter is a piece of information that we give to the function"

def say_hi():
    name = input("Enter your name: ")
    print("Hello " + name)

# say_hi() #I am calling the function, we are executing the code inside of the function. 

print("Top")
say_hi()
print("Bottom") #Is going to excecute the code in this order.


