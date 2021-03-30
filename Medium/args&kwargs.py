def printFunc(a, b, c, d):
    print(a, b, c, d)

printFunc("Debjit", "Rohan", "Harry", "Naruto")



def printFunc2(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(f"Key: {k} Value: {v}")

res = ["Debjit", "Rohan", "Harry", "Naruto"]

kwRes = {"Debjit": "Programmer", "Harry": "Tester", "Michael": "Dancer"}

printFunc2(*res, **kwRes)