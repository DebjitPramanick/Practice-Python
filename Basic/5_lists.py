tools = ["VS Code", "Android Studio", "Notepad", "Pycharm", "Sublime"]
print(tools)

print(tools[4]) # Access element by position


numbers = [2,4,5,8,1,6,3,9]

numbers.sort() # Sort the list
numbers.reverse() # Reverse list
print(numbers)

# List slice
print(numbers[0:4])

# Extended slice
print(numbers[::-2])

# Don't take less than -1 for negative slicing (Important)

# Other methods of list

print(max(numbers))
print(min(numbers))

numbers.append(10) # Append will add element to last of the list
print(numbers)

numbers.insert(5, 12) # Insert will add element to given position of the list
print(numbers)

numbers.remove(2) # Remove method removed the given element
print(numbers)

numbers.pop() # Pop method removed element from last
print(numbers)

# Tupple -----------------------------

"""
Tupple is immutable
List is mutable
"""

tupple = (1,6)
print(tupple)

