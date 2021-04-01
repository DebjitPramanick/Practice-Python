class Employee:
    def __init__(self, firstName, branch, age):
        self.firstName = firstName
        self.branch = branch
        self.age = age

    def printDetails(self):
        return f"First name is: {self.firstName}. Branch is: {self.branch}. Age is: {self.age}"


class Player:
    def __init__(self, name, game):
        self.name= name
        self.game = game

    def printInfo(self):
        return f"{self.name} is a player who plays {self.game}."


class CooolProgrammer(Employee, Player): # Here order matters
    def printData(self):
        return f"{self.firstName} is a cool programmer."



debjit = Employee("Debjit", "ECE", 21)
rohan = CooolProgrammer("Rohan", "CSE", 26)

print(rohan.printData())