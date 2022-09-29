sales = float(input("Enter sales: $"))
if sales < 1000 :
    bonus = 0.1
else:
    bonus = 0.15
reward = sales * bonus
print(reward)