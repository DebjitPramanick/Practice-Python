def printFunc():
    print("Debjit is a developer")

def addFunc(num1, num2):
    print(f"The result is {num1+num2}")


if __name__ == '__main__':
    addFunc(5,8)


"""
    If we don't use if __name__ == '__main__' the result of 
    function calls in this file, will also be shown as the 
    result of a file where this file is called.
"""