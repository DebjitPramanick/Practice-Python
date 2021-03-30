from functools import reduce

nums = [1, 5, 95, 15, 24, 6]

res = reduce(lambda x,y: x*y, nums)

print(res)