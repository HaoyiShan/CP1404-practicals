num = int(input("Number of items:"))
sum = 0
for i in range(num):
    price = float(input("Price of item:"))
    sum = sum + price
if sum > 100:
    sum = sum * 0.9
sum = format(sum,'.2f')
print("Total price for",num, "items is $",sum)