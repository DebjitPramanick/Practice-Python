myStr = "Debjit is a developer. He knows Python, Javascript."
print(myStr)

# String slice
newStr = myStr[0:6]
print(newStr)

# Advanced slice
adStr = myStr[0:10:2] # This will skip 1 character while printing till 9th character
print(adStr)

# More slice methods
moreStr = myStr[-4:-2] # Negative index starts from end of the string
print(moreStr)

# String length
print(len(myStr))

# String methods

print(myStr.isalnum()) # Checks if string alphanumeric
print(myStr.endswith("pt."))
print(myStr.count("i")) # Counts particular character
print(myStr.find("is")) # Returns starting index of given str
print(myStr.capitalize())
print(myStr.replace("Javascript", "C++"))