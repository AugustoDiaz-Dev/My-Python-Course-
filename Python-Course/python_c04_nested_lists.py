#Topic: Nested lists.

#They are called nested lists and also grids, because they have rows and columns. 

number_grid = [
[1,2,3],
[4,5,6],
[7,8,9],
[0]
]

print(number_grid[0])
print(number_grid[2][1])

for row in number_grid:
    print(row)

for row in number_grid: 
    for col in row: 
        print(col)
