var1 = 6
var2 = 8

print("Enter variable 3: ")
var3 = int(input())
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")


list = [3, 4, 6, 2]

if 4 in list:
    print("Yes it is in list.")
if 5 not in list:
    print("5 is not in list.")