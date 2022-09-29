import random

num_line = int(input("How many 'quick picks':"))
constants = []
for i in range(num_line):
    nums = []
    for i in range(6):
        nums.append(random.randint(1,45))
        nums.sort()
    constants.append(nums)
print(constants)
for num_list in constants:
    print("{} {} {} {} {} {}".format(*num_list))