#Topic: List and functions.

lucky_numbers = [2, 6 , 17, 14, 21, 48]

friends = ["Frank", "Elena", "Wilson", "Frank", "David", "YangHaoCheng", "Tina"]

friends.extend(lucky_numbers) #Joins the two lists.

print(friends)


your_friends = ["Frank", "Elena", "Wilson", "Frank", "David", "YangHaoCheng", "Tina"]

your_friends.append("Juan") #Adds an item at the end.
your_friends.insert(1, "Karen") #It doesn't replace the value, inserts it.
your_friends.remove("YangHaoCheng") #When it founds the element with the same name it removes it.

print(your_friends)

print(your_friends.clear()) #Removes all the items and gives back an empy list.


my_friends = ["Frank", "Elena", "Wilson", "Frank", "David", "Frank","YangHaoCheng", "Tina"]

my_friends.pop() #Removes the last item of the list.
print(my_friends)

print(my_friends.index("Wilson")) #Gives back the position of Wilson.
print(my_friends.count("Frank")) #Gives back how many values with the same name we have. 

print(my_friends.sort()) #Orders the list from minor to major, or in alphabetical order.

friends2 = my_friends.copy() #Makes a copy of the whole array.

your_lucky_numbers = [2, 6 , 17, 14, 21, 48]
print(your_lucky_numbers.reverse()) #Inverts the order of the values.

