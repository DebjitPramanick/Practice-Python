"""

Classes  -  Template
Object  -  Instance of the class

"""


class Student:
    colleg_year = 2
    pass # Pass means nothing is passed

debjit = Student()
rohan = Student()

debjit.firstName = "Debjit"
debjit.branch = "ECE"
debjit.age = 21

rohan.firstName = "Rohan"
rohan.branch = "CSE"
rohan.age = 20

print(debjit, rohan)
print(debjit.__dict__)

print(debjit.firstName, rohan.age)