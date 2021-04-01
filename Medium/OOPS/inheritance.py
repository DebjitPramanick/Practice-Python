class Employee:
    def __init__(self, firstName, branch, age):
        self.firstName = firstName
        self.branch = branch
        self.age = age

    def printDetails(self):
        return f"First name is: {self.firstName}. Branch is: {self.branch}. Age is: {self.age}"


class Programmer(Employee):
    def __init__(self, firstName, branch, age, lang):
        self.firstName = firstName
        self.branch = branch
        self.age = age
        self.lang = lang

    def printProg(self):
        return f"{self.firstName} is a programmer. He is expert in {self.lang}"


debjit = Employee("Debjit", "ECE", 21)

rohan = Programmer("Rohan", "CSE", 20, "Python+")

print(rohan.printProg())
print(debjit.printDetails())