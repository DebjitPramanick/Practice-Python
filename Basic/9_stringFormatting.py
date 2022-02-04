name = "Debjit"
pos = "Develoepr"
res = "My name is: %s"%name
print(res)

res2 = "{0} is a {1}"
b = res2.format(name,pos)
print(b)


# F Strings

f_string = f"This is a F String {name}. I am a {pos}."
print(f_string)
