for i in range(0,101,10):
    print(i,end=" ")

print()

for i in range(20,0,-1):
    print(i,end=" ")

print()

num = int(input("Number of stars:"))
for i in range(num):
    print("*",end="")

print()

for i in range(num):
    for x in range(i+1):
        print("*",end="")
    print()