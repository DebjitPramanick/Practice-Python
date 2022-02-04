a = 9
b = 5
c = sum((a,b)) # Built in function
print(c)


# User defined function

def function1():
    print("Hello world.")

for i in range(10):
    function1()


def function2(a,b):
    """This is a function which calculate the average of two numbers"""
    # The first line is a docstring
    avg = (a+b)/2
    print("Average is : ", avg)

function2(7,8)
print(function2.__doc__)