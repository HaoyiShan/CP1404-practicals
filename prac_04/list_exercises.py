nums = []
while len(nums) < 5:
    get_num = int(input("Number:"))
    nums.append(get_num)
print("The first number is {}".format(nums[0]))
print("The last number is {}".format(nums[-1]))
print("The smallest number is {}".format(min(nums)))
print("The largest number is {}".format(max(nums)))
print("The average of the numbers is {}".format(sum(nums)/5))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_name = input("Please input your username:")
if get_name in usernames:
    print("Access granted")
else:
    print("Access denied")