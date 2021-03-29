f = open("sample.txt")

"""

.tell() method tells the current position of f.
.seek(pos) method resets the pointer.

"""

print(f.tell())
print(f.readline())
print(f.tell())

f.seek(20) # Reset file pointer at position 20

print(f.read()) # This will start printing from 20th character

f.close()