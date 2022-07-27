print("electricity bill estimator")
CPK = float(input("Enter cents per kWh:"))
DUK = float(input("Enetr daily use in kWh:"))
NBD = float(input("Enter number of billing days:"))
EB = (CPK * DUK * NBD)/100
EB = format(EB,'.2f')
print("Estimated bill: $",EB)

print()

print("electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
TARIFF = input("Which tariff? 11 or 31:")
DUK = float(input("Enetr daily use in kWh:"))
NBD = float(input("Enter number of billing days:"))
if TARIFF == "11":
    EB = TARIFF_11 * DUK * NBD
else:
    EB = TARIFF_31 * DUK * NBD
EB = format(EB,'.2f')
print("Estimated bill: $",EB)