#Topic: For loop with ranges. 

for index in range(11):
    print(index) #Gives back numbers from 0 to 10.

for index in range(3,11):
    print(index) #Gives back numbers from 3 to 10.

for index in range(3):
    if index == 0:
        print("First iteration completed.")
    else: 
        print("Not the first one.")