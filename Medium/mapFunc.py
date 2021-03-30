

numbers = ["34", "76", "82", "59"]

nums = list(map(int, numbers))

print(nums[0] + 1)


months = ["January", "February", "March", "April"]
short_months = list(map(lambda x:x[0:3] , months))

print(short_months)


