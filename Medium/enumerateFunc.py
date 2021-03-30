

list1 = ["Python", "Java", "Cpp", "Golang", "Php", "Javascript"]

i = 1

# for item in list1:
#     if i%2 is not 0:
#         print(item)
#     i+=1

for index, item in enumerate(list1):
    if index%2 == 0:
        print(item)