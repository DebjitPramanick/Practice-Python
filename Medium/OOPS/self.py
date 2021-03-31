class Student:
    colleg_year = 2

    def __init__(self, firstName, branch, age):
        self.firstName = firstName
        self.branch = branch
        self.age = age

    def printDetails(self):
        return f"First name is: {self.firstName}. Branch is: {self.branch}. Age is: {self.age}"

    @classmethod
    def changeYear(cls,newYar):
        cls.colleg_year = newYar

    @classmethod
    def createFromStr(cls, string):
        params = string.split("-")
        return cls(params[0],params[1],int(params[2]))
        # return cls(*string.split("-")) >> This can also be done using *args


# Creating obejct using Student Class ----------------------------------------------------------------------------------

debjit = Student("Debjit", "ECE", 21)
rohan = Student("Rohan", "CSE", 20)
deba = Student("Debajeet", "ECE", 21)
bhaskar = Student.createFromStr("Bhaskar-ECE-21")

print(deba.__dict__)

deba.changeYear(3) # This will change the class instance

print(deba.colleg_year) # Output will be 3
print(debjit.colleg_year) # Output will be 3 (not 2 as class instance is changed)
print(deba.printDetails())
print(bhaskar.__dict__)