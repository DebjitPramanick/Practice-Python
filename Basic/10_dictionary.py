# Dictionary is nothing but key value pair

d1 = {"Lang": "Python", "Device": "Laptop", "IDE": "Pycharm"}
print(d1["Lang"])


# Dictionary within dictionary
d2 = {"Lang": "Python", "Device": {"Apple": "Laptop", "Windows": "Laptop"}, "IDE": "Pycharm"}
print(d2)
print(d2["Device"])
print(d2.get("Device"))

# Add and remove pairs to dictionary

d2["Exp"] = "1 Month"
print(d2)
del d2["Exp"]
print(d2)

# Update value of a key

d2.update({"Lang": "Python 3"})
print(d2)

# Copy function

d3 = d2.copy()
print(d3)
# If we use d3 = d2, changes made in d3 will also be reflected in d2


# Other functions

print(d2.items())
print(d2.keys())
print(d2.values())
