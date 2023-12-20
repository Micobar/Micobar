two_dee_list = [[1,2,3], [4,5,6], [7,8,9]]
# to access list in a list
idx = two_dee_list[0]

# to access a single variable from a list in a list
idx = two_dee_list[0][0]

for row in two_dee_list:
    print(row)
    for col in row:
        print(col)

# more readable way of putting a 2D List
        
score_list = [
[80, 60, 78, 90, 96],
[86, 78, 87, 95, 97],
[91, 95, 99, 98, 92],
[99, 98, 97, 99, 96]
]

for row in score_list:
    print(f"Term {row}")
    for col in row:
        print(f"Grade: {col}")