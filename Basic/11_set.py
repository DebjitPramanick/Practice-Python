s = set()
# Set takes only unique values

print(type(s))

s1 = set([1, 2, 3, 4])
print(s1)

# Add element to set

s1.add(5)
print(s1)

s2 = s1.union(({1, 7, 9}))
print(s2)

s3 = s1.intersection(({5,2,4}))
print(s3)

print(s1)
s1.remove(5)
print(s1)