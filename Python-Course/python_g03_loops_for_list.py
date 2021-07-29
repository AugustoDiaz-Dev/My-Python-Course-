#Topic: For loop in a LIST.

friends = ["Yang Hao Cheng", "Karen", "Francesco", "Alexandra", "Diego"]

print('The number of elements in the list is: ',len(friends)) #Gives back 5 because there are five elements in the LIST.

for index in range(len(friends)):

    print(friends[index])

print('Gives back the item is in index 2: ', friends[2])
print('Gives back the last item: ', friends[-1])

# for name in friends: 

#     print(name)

