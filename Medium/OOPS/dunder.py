class Employee:
    def __init__(self, firstName, branch, age):
        self.firstName = firstName
        self.branch = branch
        self.age = age

    def __add__(self, other): # Dunder method (Double Underscore)
        return self.age + other.age # + operator is overloaded in add method

    def __repr__(self):
        return self.firstName

'''
Mapping operators to function -> Search 0on Google
'''


emp1 = Employee("Debjit", "ECE", 21)
emp2 = Employee("Rohan", "CSE", 20)

print(emp1 + emp2, emp1.age, emp2.age)
print(emp1)
