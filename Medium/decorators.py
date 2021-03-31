def func():
    print("Subscribe now.")

func2 = func
del func # Deletes the function
func2()

def funcret(num):
    if num == 0:
        return print
    if num==-1:
        return sum


def dec1(func):
    def nowExec():
        print("Execute now.")
        func()
        print("Executed")
    return nowExec

@dec1 # >> This is method 1
def printName():
    print("My name is Debjit.")

# printName = dec1(printName) >> This is method 2
printName()
