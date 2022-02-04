# Lambda functions or anonymous functions


# Using simple function

def add(a,b):
    return a+b;

print(add(8,5))


# Using lambda function

minus = lambda x, y: x-y
print(minus(9,3))


a_first = lambda x: x[1]

a = [[2,4],[5,0],[8,2],[9,1]]
a.sort(key = a_first)
print((a))