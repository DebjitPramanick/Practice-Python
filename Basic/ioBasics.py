# File Io Basics

"""

"r" - Open file for reading
"w" - Open a file for writing
"x" - Creates file if not exists
"a" Add more content to a file
"t" - text mode
"b" - binary mode
"+" — read and write

"""



# File writing

f = open("sample.txt", "r") # Opening file in read mode
content = f.read()
print(content)

print("Read line")


f = open("sample.txt", "rt") # Opening file in read mode
# content = f.readline()
# print("Firsst line - ", content)

content = f.readlines()
print("All lines - ", content)

f.close()