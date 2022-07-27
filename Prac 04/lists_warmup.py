numbers = [3, 1, 4, 1, 5, 9, 2]
"""
(1) 3
(2) 2
(3) 1
(4) [3, 1, 4, 1, 5, 9]
(5) [1]
(6) True
(7) False
(8) False
(9) [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

"""
Change the first element of numbers to "ten" (the string, not the number 10)
Change the last element of numbers to 1
Get all the elements from numbers except the first two (slice)
Check if 9 is an element of numbers
"""
numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
