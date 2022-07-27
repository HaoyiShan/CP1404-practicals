def main():
    password = get_password()
    l = len(password)
    for i in range(l):
        print("*", end="")


def get_password():
    print("Please enter password")
    password = input("> ")
    return password


main()