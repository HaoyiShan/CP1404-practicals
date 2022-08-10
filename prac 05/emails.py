Get_email = input("Please enter your email:")
Get_name = input("Please enter your username:")
name_email = {}
while Get_email != "":
    name_email[Get_email] = Get_name
    Get_email = input("Please enter your email:")
    Get_name = input("Please enter your username:")


def Name_correct():
    for email in name_email:
        print("Email:", email)
        check = input("Is your name {}? (y/n)".format(name_email[email]))
        if check == "n":
            new_name = input("Correct Name:")
            name_email[email] = new_name


Name_correct()

for i in name_email.items():
    print(i)