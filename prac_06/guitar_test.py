from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year}")

guitar = Guitar(name, year, cost)
print(guitar)
print(guitar.get_age())

