from guitar import Guitar

guitar_list = []
print("My guitars!")


def main():
    while True:
        name = input("Name:")
        if name != "":
            year = int(input("Year:"))
            cost = int(input("Cost:"))
            guitar = Guitar(name, year, cost)
            guitar_list.append(guitar)
            print(guitar, "added.")
        else:
            break
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print(guitar_list)
    show_guitar(guitar_list)


def show_guitar(g_list):
    num = 1
    print("\n")
    print("These are my guitars:")
    for i in g_list:
        vintage_string = " (vintage)" if i.is_vintage() else ""
        print(f"Guitar {num}: {i.name:>20} ({i.year}), worth ${i.cost:10.2f} {vintage_string}")
        num = num + 1


main()
