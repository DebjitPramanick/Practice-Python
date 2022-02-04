list = [34, 56, 23, 56]

for i in list:
    print(i, end=" ")
print()
list1 = [ ["Debjit", 1], ["Rohan", 2], ["Deba", 4]]

for i , j in list1:
    print(i , j)


items = [4, 20, 17, 6, 30, 5, 10, 3]

for i in items:
    if str(i).isnumeric() and i>6:
        print(i)