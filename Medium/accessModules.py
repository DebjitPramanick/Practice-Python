import random

for i in range(5):
    random_num = random.randint(0, 2000)
    print(random_num)

rand = random.random() * 1000
print(rand)

# Chooose randomly

list = ["Debjit", "Deba", "Rohan", "Bhaskar", "Ashis"]
choice = random.choice(list)
print(choice)

