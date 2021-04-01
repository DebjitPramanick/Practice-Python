class Level1:
    levelIndex = 1
    def printDetails1(self):
        return f"Level1 class is a class of level {self.levelIndex} in multilevel inheritance."

class Level2(Level1):
    levelIndex = 2
    def printDetails2(self):
        return f"Level2 class is a class of level {self.levelIndex} in multilevel inheritance."

class Level3(Level2):
    levelIndex = 3
    def printDetails3(self):
        return f"Level3 class is a class of level {self.levelIndex} in multilevel inheritance."



l1 = Level1()
l2 = Level2()
l3 = Level3()

print(l1.printDetails1())
print(l2.printDetails2())
print(l3.printDetails3())


print(l3.printDetails1())
print(l2.printDetails1())
print(l3.printDetails2())
