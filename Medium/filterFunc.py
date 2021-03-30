ages = [5, 7, 87, 24, 12, 20, 21, 3, 67, 34, 29, 25, 50, 56, 44, 43]

agesLess30 = list(filter(lambda x:x<=30, ages))
agesGreater30 = list(filter(lambda x:x>=30, ages))

print(f"The number of under 30 aged people: {len(agesLess30)}")
print(f"The number of above 30 aged people: {len(agesGreater30)}")

maxGroup = max(len(agesGreater30), len(agesLess30))

if maxGroup == len(agesLess30):
    print("The group of under 30 aged people is major.")
else:
    print("The group of above 30 aged people is major.")
